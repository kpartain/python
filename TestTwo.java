public class TestTwo {
        public static void main(String[]args) {
            String road1 = ".X..X"; //2
            System.out.println("ROAD 1 EXPECT 2 " + setsOfThreeWithPotholes(road1));
            System.out.println("\n\n");
            String road2 = "X.X XXX X.X."; //3
            System.out.println("ROAD 2 EXPECT 3 " + setsOfThreeWithPotholes(road2));
            System.out.println("\n\n");
            String road3 = "XX.XXX.."; //2
            System.out.println("ROAD 3 EXPECT 2 " + setsOfThreeWithPotholes(road3));
            System.out.println("\n\n");
            String road4 = "XXX X"; //2
            System.out.println("ROAD 4 EXPECT 2 " + setsOfThreeWithPotholes(road4));
            System.out.println("\n\n");
        }
    
        public static int setsOfThreeWithPotholes(String road) {
            int setsFixed = 0;
            boolean xFound = false;
            int lastIndex = road.length() -1;
            for(int i = 0; i != lastIndex; i++){
                while(!xFound) {
                    if(road.charAt(i) == '.'){
                        i++;
                    }  else if (road.charAt(i) == 'X') {
                        System.out.println("Found first X at " + i);
                        xFound = true;
                        setsFixed++;
                        i+=2;
                    }
                }
                String newString = "";
                if(i <= lastIndex-2){
                    newString += Character.toString(road.charAt(i));
                    i++;
                    newString += Character.toString(road.charAt(i));
                    i++;
                    newString += Character.toString(road.charAt(i));
                    i++;
                } else if(i <= lastIndex-1) {
                    newString += Character.toString(road.charAt(i));
                    i++;
                    newString += Character.toString(road.charAt(i));
                    i++;
                } else if (i == lastIndex) {
                    newString += Character.toString(road.charAt(i));
                    i++;
                }
                System.out.println(newString);
                if(newString.contains("X")){
                    setsFixed++;
                }
            }
            return setsFixed;
        }
    }