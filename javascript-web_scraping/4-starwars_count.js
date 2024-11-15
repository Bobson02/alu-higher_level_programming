#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    const wedgeId = '18';
    const movieCount = films.reduce((count, film) => {
      return film.characters.some(character => character.endsWith(`/${wedgeId}/`)) ? count + 1 : count;
    }, 0);
    console.log(movieCount);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
