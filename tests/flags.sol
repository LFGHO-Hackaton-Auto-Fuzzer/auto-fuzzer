contract Test {
  event Flag(bool);

  bool private flag0 = true;
  bool private flag1 = true;

  function set0(int val) public returns (bool){
    if (val % 100 == 0) 
      flag0 = false;
  }

  function set1(int val) public returns (bool){
    if (val % 10 == 0 && !flag0) 
      flag1 = false;
  }

}
