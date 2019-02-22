is_even<-function(x){
  if(as.numeric(x)%%2==0 & as.numeric(x)!=0){
    "True"
  }
    else{
      "False"
    }
  }

is_even(6)
is_even(5)
is_even(0)
