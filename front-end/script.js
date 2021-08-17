function rangeSlide(value) {
    document.getElementById('rangeValue').innerHTML = value;
}

$(document).ready(() => {

    $('#result').hide()
    $('form').on('submit', event => {
    
        event.preventDefault();
    
        var sibsp =$("#sibsp").val();
        var age =$("#age").val();
        var sex =$("#sex").val();
        var fare = $("#fare").val();
        var pclass =$("#pclass").val();
        var embarked =$("#embarked").val();
    
        url =`https://titanicfastapi.azurewebsites.net/prediction/?pclass=${pclass}&sex=${sex}&age=${age}&sibsp=${sibsp}&fare=${fare}&embarked=${embarked}`;
        
        // fetch(url)
        // .then(response => response.json())
        // .then(data =>
        //     console.log(data)
        // ) 
    
        $.ajax({
            url: url, 
            type: "GET", 
            dataType: "json",
        })
        .done(function (json) {
            text = json['description']
            console.log(text)
            $('#result').text(text)
            $('#result').fadeIn()
        })
    
    })
    
    });
    