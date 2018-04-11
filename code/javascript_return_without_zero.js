var data = [0, 1, 2, 'stop', 2, 0, 1, 'stop'];

function checkwithoutzero(data) {
    return data!= 0 ;
}

function myFunction() {
    document.getElementById("demo").innerHTML = data.filter(checkwithoutzero);
}
