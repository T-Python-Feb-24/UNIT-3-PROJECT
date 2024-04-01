function myconfirm() {
    if (confirm('Are You sure you want to delete?')) {
        document.getElementById("delete").click();
    } else {
        return false;
    }
}

var check = function () {
    if (document.getElementById('password').value ==
        document.getElementById('confirm_password').value) {
        document.getElementById('message').style.color = 'green';
        document.getElementById('message').innerHTML = 'متطابقة';
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = 'غير متطابقة';
    }
}