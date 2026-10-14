package jo.almaher.api;
import java.util.*;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.*;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;
@RestControllerAdvice
public class ApiErrors {
 @ExceptionHandler(NoSuchElementException.class)
 ResponseEntity<Map<String,String>> missing(NoSuchElementException ex){return ResponseEntity.status(404).body(Map.of("error","Not found"));}
 @ExceptionHandler(MethodArgumentNotValidException.class)
 ResponseEntity<Map<String,String>> invalid(MethodArgumentNotValidException ex){return ResponseEntity.badRequest().body(Map.of("error","Invalid request","field",ex.getBindingResult().getFieldErrors().stream().findFirst().map(e->e.getField()).orElse("request")));}
 @ExceptionHandler(DataIntegrityViolationException.class)
 ResponseEntity<Map<String,String>> conflict(DataIntegrityViolationException ex){return ResponseEntity.status(409).body(Map.of("error","Duplicate or invalid record"));}
 @ExceptionHandler(org.springframework.http.converter.HttpMessageNotReadableException.class)
 ResponseEntity<Map<String,String>> malformed(Exception ex){return ResponseEntity.badRequest().body(Map.of("error","Malformed request"));}
}