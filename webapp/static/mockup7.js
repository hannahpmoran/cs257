/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 *
 * A little bit of Javascript showing one small example of AJAX
 * within the "books and authors" sample for Carleton CS257.
 *
 * This example uses a very simple-minded approach to Javascript
 * program structure. We'll talk more about this after you get
 * a feel for some Javascript basics.
 */

window.onload = initialize;

function initialize() {
    mockup7Test()
}

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function mockup7Test() {
    var url = getAPIBaseURL() + '/mockup7';

    // send request to our api
    fetch(url, {method: 'get'})

    // get info back convert to json
    .then((response) => response.json())

    // now build html page body
    .then(function(artist_list) {
        var artist_name = '';
        var artist_info_div = '';

    // build this
        artist_name = artist_list['artist_firstname'] + ' ' + artist_list['artist_surname'];
        <h2><center>Sir Wombat the Artiste</center></h2>

        artist_info_div = '<div id = "image-page"> <div class="current-image"> <img src = "wombat.jpg"  alt = "a wombat strolling over to you">  </div> <div class = "image-detail"> ' + artist_list['artist_bio'] + ' Artist Bio:</div> <div class = "image-detail">' + artist_list['artist_birthyear'] + '-' + artist_list['artist_deathyear'] + 'XXXX-YYYY</div> <div class = "image-detail"> # of works at the MET:</div> </div>';

        var resultsTableElement = document.getElementById('artist_names');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = artist_name;
        }
        var resultsTableElement = document.getElementById('artist_info_div');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = artist_info_div;
        }
    })

    .catch(function(error) {
        console.log(error);
    });

}

