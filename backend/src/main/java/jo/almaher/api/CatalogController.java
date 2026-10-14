package jo.almaher.api;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import java.util.*;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;
@RestController
public class CatalogController {
 private final CatalogRepository repo;
 public CatalogController(CatalogRepository repo){this.repo=repo;}
 public record Input(@NotNull CatalogEntry.Category category,
   @NotBlank @Pattern(regexp="[a-z0-9]+(?:-[a-z0-9]+)*") @Size(max=120) String slug,
   @NotBlank @Size(max=300) String titleAr,@NotBlank @Size(max=300) String titleEn,
   @Size(max=10000) String bodyAr,@Size(max=10000) String bodyEn,
   @Size(max=1000) String imageUrl,boolean published,int displayOrder){}
 @GetMapping("/api/v1/catalog/{category}")
 public List<CatalogEntry> listPublic(@PathVariable CatalogEntry.Category category){return repo.findByCategoryAndPublishedTrueOrderByDisplayOrderAsc(category);}
 @GetMapping("/api/v1/catalog/{category}/{slug}")
 public CatalogEntry publicItem(@PathVariable CatalogEntry.Category category,@PathVariable String slug){
  return repo.findByCategoryAndSlugAndPublishedTrue(category,slug).orElseThrow(()->new NoSuchElementException("Not found"));
 }
 @GetMapping("/api/v1/admin/catalog")
 public List<CatalogEntry> listAdmin(){return repo.findAll();}
 @PostMapping("/api/v1/admin/catalog")
 public ResponseEntity<CatalogEntry> create(@Valid @RequestBody Input input){
  CatalogEntry entry=apply(new CatalogEntry(),input);
  return ResponseEntity.status(HttpStatus.CREATED).body(repo.saveAndFlush(entry));
 }
 @PutMapping("/api/v1/admin/catalog/{id}")
 public CatalogEntry update(@PathVariable UUID id,@Valid @RequestBody Input input){
  CatalogEntry entry=repo.findById(id).orElseThrow(()->new NoSuchElementException("Not found"));
  return repo.saveAndFlush(apply(entry,input));
 }
 @DeleteMapping("/api/v1/admin/catalog/{id}")
 public ResponseEntity<Void> delete(@PathVariable UUID id){
  if(!repo.existsById(id))throw new NoSuchElementException("Not found");
  repo.deleteById(id);return ResponseEntity.noContent().build();
 }
 private CatalogEntry apply(CatalogEntry e,Input r){
  e.category=r.category();e.slug=r.slug();e.titleAr=r.titleAr();e.titleEn=r.titleEn();
  e.bodyAr=r.bodyAr();e.bodyEn=r.bodyEn();e.imageUrl=r.imageUrl();
  e.published=r.published();e.displayOrder=r.displayOrder();return e;
 }
}