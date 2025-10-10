int channel[8];

void readChannel() {
  String s = ""; 
  String d = "";
  String k = " ";

  while (Serial1.available() > 0) {  
    char c = Serial1.read();
    s += c;

    int start = s.indexOf('<');      
    int end = s.indexOf('>');         

    if (c == '>') {
      d = s.substring(start + 1, end);
      s = "";                          
    }

    int index = 0;
    k = " ";

    for (int i = 0; i < d.length(); i++) {
      if (d[i] != ' ') {
        k += d[i];
      } else {
        if (index < 8) {
          channel[index] = k.toInt();  
          index++;
        }
        k = " "; 
      }
    }
    if (k != " " && index < 8) {
      channel[index] = k.toInt();
    }
  }
}

void loop() {
  readChannel();
}
