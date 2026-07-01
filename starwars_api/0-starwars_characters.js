#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  function printCharacter (i) {
    request(characters[i], function (err2, res2, body2) {
      if (err2) {
        console.error(err2);
        return;
      }

      const character = JSON.parse(body2);
      console.log(character.name);

      if (i + 1 < characters.length) {
        printCharacter(i + 1);
      }
    });
  }

  printCharacter(0);
});
