#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the same order of
// the list “characters” in the /films/ response.
// endpoint: https://swapi-api.hbtn.io/api/films/:id
// ./101-starwars_characters.js 3

const request = require('request');

function helpRequest (arr, i) {
  if (i === arr.length) {
    return;
  }
  request(arr[i], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).name);
    helpRequest(arr, i + 1);
  });
}

request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const charac = JSON.parse(body).characters;
  helpRequest(charac, 0);
});


