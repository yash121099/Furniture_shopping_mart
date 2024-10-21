
function validateSignup(){
    var fullName = document.getElementById("fname").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("passw").value;
    var cPassword = document.getElementById("cpassw").value;
    var mobile = document.getElementById("mobile").value;

    var emailRegx = /^([a-zA-Z0-9\.-]+)@([a-zA-Z-0-9-]+).([a-z]{2,8})(.[a-z]{2,8})?$/;

    var mobileRegex = /^[6-9][0-9]{9}$/;
            
    if(fullName.trim()=="" ){
      alert("Enter Full Name");
      return false;
    }
    else if(email.trim()=="" ){
      alert("Enter Email");
      return false;
    }
    else if(!emailRegx.test(email)){
        alert("Enter valid Email");
        return false;
    }
    else if(mobile.trim()==""){
      alert("Enter Mobile Number");
      return false;
    }
    else if(!mobileRegex.test(mobile)){
      alert("Enter valid Mobile Number");
      return false;
    }
    else if(password.trim()==""){
      alert("Enter Password");
      return false;
    }
    else if(cPassword.trim()==""){
      alert("Enter Confirm Password");
      return false;
    }
    else if(cPassword.trim()!=password.trim()){
      alert("Enter same Password and Conform Password");
      return false;
    }
    else if(password.trim().length<8){
      alert("Password too short");
      return false;
    }    
    else{
      return true;
    }
  } 


  function showPwd(id, el) {
    let x = document.getElementById(id);
    if (x.type === "password") {
      x.type = "text";
      el.className = 'fa fa-eye-slash showpwd';
    } else {
      x.type = "password";
      el.className = 'fa fa-eye showpwd';
    }
  }