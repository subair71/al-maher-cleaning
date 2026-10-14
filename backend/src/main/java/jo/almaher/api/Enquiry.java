package jo.almaher.api;
import jakarta.persistence.*;
import java.time.*;
import java.util.UUID;
@Entity @Table(name="enquiries")
public class Enquiry {
  public enum Kind {QUOTE, BOOKING, CORPORATE, CONTACT}
  public enum Status {NEW, CONTACTED, QUOTED, CONFIRMED, COMPLETED, CANCELLED}
  @Id public UUID id;
  @Enumerated(EnumType.STRING) @Column(nullable=false) public Kind kind;
  @Column(nullable=false) public String name;
  @Column(nullable=false) public String phone;
  public String email;
  @Column(name="service_slug") public String serviceSlug;
  public String city;
  public String address;
  @Column(name="requested_date") public LocalDate requestedDate;
  @Column(name="preferred_time") public String preferredTime;
  public String message;
  @Column(nullable=false) public String language;
  @Column(nullable=false) public boolean consent;
  @Enumerated(EnumType.STRING) @Column(nullable=false) public Status status;
  @Column(name="created_at",nullable=false) public Instant createdAt;
  @Column(name="updated_at",nullable=false) public Instant updatedAt;
  @PrePersist void create() {if(id==null)id=UUID.randomUUID();status=Status.NEW;createdAt=Instant.now();updatedAt=createdAt;}
  @PreUpdate void update(){updatedAt=Instant.now();}
}