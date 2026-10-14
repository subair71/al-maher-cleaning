package jo.almaher.api;
import jakarta.persistence.*;
import java.time.Instant;
import java.util.UUID;
@Entity @Table(name="catalog_entries",uniqueConstraints=@UniqueConstraint(columnNames={"category","slug"}))
public class CatalogEntry {
 public enum Category {SERVICE,OFFER,FAQ,REVIEW,CLIENT,GALLERY,BEFORE_AFTER,LANDING_PAGE,SITE_CONTENT}
 @Id public UUID id;
 @Enumerated(EnumType.STRING) @Column(nullable=false) public Category category;
 @Column(nullable=false) public String slug;
 @Column(name="title_ar",nullable=false) public String titleAr;
 @Column(name="title_en",nullable=false) public String titleEn;
 @Column(name="body_ar",columnDefinition="text") public String bodyAr;
 @Column(name="body_en",columnDefinition="text") public String bodyEn;
 @Column(name="image_url") public String imageUrl;
 @Column(nullable=false) public boolean published;
 @Column(name="display_order",nullable=false) public int displayOrder;
 @Column(name="created_at",nullable=false) public Instant createdAt;
 @Column(name="updated_at",nullable=false) public Instant updatedAt;
 @PrePersist void create(){if(id==null)id=UUID.randomUUID();createdAt=Instant.now();updatedAt=createdAt;}
 @PreUpdate void update(){updatedAt=Instant.now();}
}