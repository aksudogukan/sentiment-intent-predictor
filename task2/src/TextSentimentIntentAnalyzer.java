import java.io.IOException;
import java.util.Scanner;

public class TextSentimentIntentAnalyzer {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        // Specify the full path to your Python script
        String pythonScriptPath = "C:/Users/dogukan/Desktop/TEB/task1/src/sentiment_intent_predictor.py";

        while (true) {
            System.out.println("Please enter your text? (type 'q' to quit): ");
            String inputText = scanner.nextLine();

            if (inputText.equalsIgnoreCase("q")) {
                break;
            }

            // ProcessBuilder for calling python code
            ProcessBuilder processBuilder = new ProcessBuilder("python", pythonScriptPath, inputText);
            Process process = processBuilder.start();

            // Read ouput of python code
            java.io.InputStream inputStream = process.getInputStream();
            java.util.Scanner s = new java.util.Scanner(inputStream).useDelimiter("\\A");
            String output = s.hasNext() ? s.next() : "";

            // Print output of python side
            System.out.println("Python Output:");
            System.out.println(output);
        }

        // Kullanýcýdan gelen veriyi almayý bitir
        scanner.close();
    }
}
