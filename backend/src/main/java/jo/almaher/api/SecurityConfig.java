package jo.almaher.api;
import java.util.Arrays;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.factory.PasswordEncoderFactories;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import org.springframework.security.config.http.SessionCreationPolicy;
@Configuration
public class SecurityConfig {
  @Bean PasswordEncoder encoder() {return PasswordEncoderFactories.createDelegatingPasswordEncoder();}
  @Bean UserDetailsService users(@Value("${app.admin.username}") String username,@Value("${app.admin.password}") String password, PasswordEncoder encoder) {
    if (password.isBlank() || password.length() < 16) throw new IllegalStateException("Set ADMIN_PASSWORD (minimum 16 characters)");
    return new InMemoryUserDetailsManager(User.withUsername(username).password(encoder.encode(password)).roles("ADMIN").build());
  }
  @Bean SecurityFilterChain security(HttpSecurity http) throws Exception {
    return http.csrf(csrf->csrf.disable()).cors(Customizer.withDefaults())
      .sessionManagement(s->s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
      .authorizeHttpRequests(a->a
        .requestMatchers("/actuator/health","/actuator/info").permitAll()
        .requestMatchers(HttpMethod.POST,"/api/v1/enquiries").permitAll()
        .requestMatchers(HttpMethod.GET,"/api/v1/catalog/**").permitAll()
        .requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
        .anyRequest().denyAll())
      .httpBasic(Customizer.withDefaults()).build();
  }
  @Bean CorsConfigurationSource cors(@Value("${app.cors.origins}") String origins) {
    CorsConfiguration c=new CorsConfiguration();
    c.setAllowedOrigins(Arrays.stream(origins.split(",")).map(String::trim).toList());
    c.setAllowedMethods(Arrays.asList("GET","POST","PUT","PATCH","DELETE","OPTIONS"));
    c.setAllowedHeaders(Arrays.asList("Authorization","Content-Type"));
    c.setMaxAge(3600L);
    UrlBasedCorsConfigurationSource source=new UrlBasedCorsConfigurationSource();
    source.registerCorsConfiguration("/api/**",c); return source;
  }
}