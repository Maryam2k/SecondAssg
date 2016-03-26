
import java.io.IOException;
import java.util.*;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.conf.Configuration;

public class KNNReducer extends Reducer <RecordKey, RecordKey, Text, Text> {
  
  // the "k" to use in the KNN classification
  private int k;
  
  protected void setup (Context context) throws IOException, InterruptedException {
    
    // first we look for the number of NN points to use
    Configuration conf = context.getConfiguration ();
    
    // if we can't find it in the configuration, then die
    if (conf.get ("k") == null)
      throw new RuntimeException ("no k was found!");
    k = Integer.parseInt (conf.get ("k"));
  }
  
  public void reduce (RecordKey key, Iterable <RecordKey> values, Context context) throws IOException, InterruptedException {
    // your code goes here!
  }
  
}

