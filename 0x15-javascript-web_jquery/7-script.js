$.ajax({
    url: "https://swapi.co/api/people/5/?format=json",
    type: "GET",
    dataType : "json",
})
    .done(function( json ) {
        $( "DIV#character" ).text( json.name );
    });
