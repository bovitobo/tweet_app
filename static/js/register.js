// Look at console
$(document).ready(function() {
	var loginUsername;
	var loginPassword;
	var account = [loginUsername, loginPassword];

	$('#login-button').on('click', function() {
		var loginUsernameEntry = $("#login-username").val();
		var loginPasswordEntry = $("#login-password").val();
		if (loginUsernameEntry == account[0] && loginPasswordEntry == account[1]) {
			console.log("Current Username " + account[0]);
			console.log("Current Password " + account[1]);
			console.log("Logged In");
		} else {
			console.log("Attempted Username " + loginUsernameEntry);
			console.log("Attempted Password " + loginPasswordEntry);
			console.log("Login Falied");
		};
	});

	$('#create-button').on('click', function() {
		var createUsernameEntry = $("#create-username").val();
		var createPasswordEntry = $("#create-password").val();
		var createEmailEntry = $("#create-email").val();
        var createUsernameValid = false;
        var createPasswordValid = false;
        var createEmailValid = false;
        var createUsernameObject = $("#create-username");
        var createPasswordObject = $("#create-password");
        var createEmailObject = $("#create-email");
        var validate = /^\s*[a-zA-Z0-9,\s]+\s*$/;
        var validateEmail = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

        if(!validate.test(createUsernameEntry) || (createUsernameEntry).length == 0) {
          $(createUsernameObject).addClass("error")
          $(createUsernameObject).val("No special characters or spaces.")
        } else {
          createUsernameValid = true;
          var username = $(createUsernameObject).val();
        }

        if(!validate.test(createPasswordEntry) || (createPasswordEntry).length == 0) {
          $(createPasswordObject).addClass("error");
          $(createPasswordObject).val("No special characters or spaces.");
        } else {
          createPasswordValid = true;
          var password = $(createPasswordObject).val();
        }

        if(!validateEmail.test(createEmailEntry)) {
          $(createEmailObject).addClass("error");
          $(createEmailObject).val("Enter a valid email");
        } else {
          createEmailValid = true;
          var email = createEmailObject.val();
        }

        $(createUsernameObject).on('click', function () {
          $(this).val("");
          $(this).removeClass("error");
        });

        $(createPasswordObject).on('click', function () {
          $(this).val("");
          $(this).removeClass("error");
        });

        $(createEmailObject).on('click', function () {
          $(this).val("");
          $(this).removeClass("error");
        });

		console.log("Account Username " + username);
		console.log("Account Password " + password);
		console.log("Email " + email);

		if(createUsernameValid == true && createPasswordValid == true && createEmailValid == true) {
          $.ajax({
                url:'register',
                type:'post',
                data:{action:'register',username:username,password:password,email:email},
                success:function(response){
                    if(response == 'success'){
                        window.location = "/tweet_app";
                    }else{
                        msg = "Invalid username and password!";
                    }
                    $("#message").html(msg);
                }
            });
        }
	});

	$('.message a').on('click', function() {
		$('form').animate({
			height: "toggle",
			opacity: "toggle"
		}, "fast");
	});
});