package Puzzles.RomanToInteger;
import java.util.HashMap;

class RomanToInteger {
    public int romanToInt(final String s) {
        int output = 0;
        int previous = 0;
        int i = s.length() - 1;
        HashMap<String, Integer> key = new HashMap<>(7, 1);
        key.put("I", 1);
        key.put("V", 5);
        key.put("X", 10);
        key.put("L", 50);
        key.put("C", 100);
        key.put("D", 500);
        key.put("M", 1000);

        while (i >= 0) {
            final int current = key.get(s.substring(i, i + 1));
            if (previous > current){
                output -= current;
            }else {
                output += current;
            }
            previous = current;
            i--;
        }
        return output;
    }
}
