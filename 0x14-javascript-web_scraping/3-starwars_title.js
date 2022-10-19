#!/usr/bin/node
// Script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
// endpoint: https://swapi-api.hbtn.io/api/films/:id
// ./3-starwars_title.js 5

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return (console.error(error));
  }
  console.log(JSON.parse(body).title);
});
