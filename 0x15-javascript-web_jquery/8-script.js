$.ajax({
    url: "https://swapi.co/api/films/?format=json",
    type: "GET",
    dataType : "json",
})
    .done(function( json ) {
        for (val of json.results) {
            $( "UL#list_movies" ).append("<li>" + val.title + "</li>");
        }
    });
