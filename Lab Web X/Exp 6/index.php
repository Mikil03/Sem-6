<html>

<head>
    <script>
        function showHint(str) {
            if (str.length == 0) {
                document.getElementById("txtHint").innerHTML = "Name can't be empty";
                return;
            } else {
                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById("txtHint").innerHTML = this.responseText;
                    }
                };
                xhr.open("GET", "gethint.php?q=" + str + "&c=", true);
                xhr.send();
            }
        }

        function showCollege(str) {
            if (str.length == 0) {
                document.getElementById("txtHint").innerHTML = "College Name can't be empty";
                return;
            } else {
                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById("txtHint").innerHTML = this.responseText;
                    }
                };
                xhr.open("GET", "gethint.php?c=" + str + "&q=", true);

                xhr.send();
            }
        }

        function retypePwd(str) {
            var pwd = document.getElementById("pwd").value;
            if (str.length == 0) {
                document.getElementById("txtHint").innerHTML = "Password can't be empty";
            } else if (str != pwd) {
                document.getElementById("txtHint").innerHTML = "Password should be same as of above field";
            } else if (str == pwd) {
                document.getElementById("txtHint").innerHTML = "Successfully Registered!! Thank you";
            }
        }
    </script>
</head>

<body>
    <p><b>Start typing a name in the input field below:</b></p>
    <form>
        Full Name: <input type="text" onkeyup="showHint(this.value)"><br><br>
        College Name: <input type="text" onkeyup="showCollege(this.value)"><br><br>
        Password: <input type="password" id="pwd"><br><br>
        Retype Password: <input type="password" onkeyup="retypePwd(this.value)"><br><br>
        <input type="submit" value="Submit">
    </form>
    <p>Suggestions: <span id="txtHint"></span></p><br><br>
</body>

</html>