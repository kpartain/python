public class RoadWork {
    public static void main(String[]args) {
        String road1 = ".X..X"; //2
        System.out.println(countSetsOfPotholesFixed(road1));
        String road2 = "X.XXXXX.X."; //4
        System.out.println(countSetsOfPotholesFixed(road2));
        String road3 = "XX.XXX.."; //2
        System.out.println(countSetsOfPotholesFixed(road3));
        String road4 = "XXX X"; //2
        System.out.println(countSetsOfPotholesFixed(road4));
    }

    public static int countSetsOfPotholesFixed(String road) {
        int setsFixed = 0;
        for(int i = 0; i < road.length(); i++){
            int xsInARow = 0;
            if(road.charAt(i) == '.'){
                //OK road, reset xsInARow
                xsInARow = 0;
            } else if(road.charAt(i) == 'X'){
                //can increment i & xs in a row
                xsInARow++;
                if(i+1 < road.length()) {
                    while(road.charAt(i+1) == 'X' && xsInARow <2) {
                    xsInARow++;
                    i++;
                    }
                    xsInARow = 0;
                    i++;
                }
                setsFixed++;
            }
        }
        return setsFixed;
    }
}
