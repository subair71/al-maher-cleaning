package jo.almaher.api;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.UUID;
public interface EnquiryRepository extends JpaRepository<Enquiry,UUID> {}