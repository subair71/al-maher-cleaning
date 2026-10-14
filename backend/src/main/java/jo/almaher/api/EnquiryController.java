package jo.almaher.api;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import java.time.LocalDate;
import java.util.*;
import org.springframework.data.domain.*;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
@RestController
public class EnquiryController {
  private final EnquiryRepository repo;
  public EnquiryController(EnquiryRepository repo){this.repo=repo;}
  public record Request(
    @NotNull Enquiry.Kind kind,
    @NotBlank @Size(max=120) String name,
    @NotBlank @Pattern(regexp="^[+0-9()\\s-]{7,35}$") String phone,
    @Email @Size(max=254) String email,
    @Size(max=100) String serviceSlug,
    @Size(max=120) String city,
    @Size(max=500) String address,
    @FutureOrPresent LocalDate requestedDate,
    @Size(max=80) String preferredTime,
    @Size(max=5000) String message,
    @Pattern(regexp="ar|en") String language,
    @AssertTrue boolean consent){}
  public record Receipt(UUID id,String status){}
  @PostMapping("/api/v1/enquiries")
  public ResponseEntity<Receipt> create(@Valid @RequestBody Request r) {
    Enquiry e=new Enquiry();
    e.kind=r.kind();e.name=r.name().trim();e.phone=r.phone().trim();e.email=r.email();
    e.serviceSlug=r.serviceSlug();e.city=r.city();e.address=r.address();
    e.requestedDate=r.requestedDate();e.preferredTime=r.preferredTime();
    e.message=r.message();e.language=r.language()==null?"ar":r.language();e.consent=r.consent();
    Enquiry saved=repo.save(e);
    return ResponseEntity.status(HttpStatus.CREATED).body(new Receipt(saved.id,saved.status.name()));
  }
  @GetMapping("/api/v1/admin/enquiries")
  public Page<Enquiry> list(@RequestParam(defaultValue="0") int page,@RequestParam(defaultValue="20") int size){
    return repo.findAll(PageRequest.of(Math.max(0,page),Math.min(100,Math.max(1,size)),Sort.by(Sort.Direction.DESC,"createdAt")));
  }
  @GetMapping("/api/v1/admin/enquiries/{id}")
  public Enquiry get(@PathVariable UUID id){return repo.findById(id).orElseThrow(()->new NoSuchElementException("Enquiry not found"));}
  public record StatusUpdate(@NotNull Enquiry.Status status){}
  @PatchMapping("/api/v1/admin/enquiries/{id}/status")
  public Enquiry status(@PathVariable UUID id,@Valid @RequestBody StatusUpdate r){
    Enquiry e=get(id);e.status=r.status();return repo.save(e);
  }
}