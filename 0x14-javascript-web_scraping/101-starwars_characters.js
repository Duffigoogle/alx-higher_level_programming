#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the same order of
// the list “characters” in the /films/ response.
// endpoint: https://swapi-api.hbtn.io/api/films/:id
// ./101-starwars_characters.js 3

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

// wrap a request in an promise
function getCharacter (uri) {
  return new Promise((resolve, reject) => {
    request(uri, (error, response, body) => {
      if (error) reject(error);
      resolve(body);
    });
  });
}

// now to program the "usual" way
// all you need to do is use async functions and await
// for functions returning promises
async function myBackEndLogic (listUri) {
  try {
    for (const uri of listUri) {
      const data = await getCharacter(uri);
      console.log(JSON.parse(data).name);
    }
  } catch (error) {
    console.error('ERROR:');
    console.error(error);
  }
}

// get list of characters url
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    // console.log(charactersList)
    myBackEndLogic(characters);
  }
});
