package jo.almaher.api;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.*;
public interface CatalogRepository extends JpaRepository<CatalogEntry,UUID> {
 List<CatalogEntry> findByCategoryAndPublishedTrueOrderByDisplayOrderAsc(CatalogEntry.Category category);
 Optional<CatalogEntry> findByCategoryAndSlugAndPublishedTrue(CatalogEntry.Category category,String slug);
}