import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ApiPostTest {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://127.0.0.1:8000/students/create");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            // Set headers
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json; utf-8");
            conn.setDoOutput(true);

            // JSON data
            String jsonInputString = "{\"name\": \"Rubhii\", \"age\": 18, \"email\": \"ruhi77@gmail.com\"}";

            // Send request
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            // Read response
            int responseCode = conn.getResponseCode();
            System.out.println("Response Code: " + responseCode);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
