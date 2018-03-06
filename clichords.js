const ugs = require('ultimate-guitar-scraper')
const Table = require('cli-table2');
const colors = require('colors');
const prompt = require('prompt');
var table = new Table({
  chars: {
    'top': '═',
    'top-mid': '╤',
    'top-left': '╔',
    'top-right': '╗',
    'bottom': '═',
    'bottom-mid': '╧',
    'bottom-left': '╚',
    'bottom-right': '╝',
    'left': '║',
    'left-mid': '╟',
    'mid': '─',
    'mid-mid': '┼',
    'right': '║',
    'right-mid': '╢',
    'middle': '│'
  }
});
prompt.start();


function listTabs(tabs) {

  table.push([colors.yellow("ID"), colors.yellow('Artist'), colors.yellow('Title'), colors.yellow('Rating'), colors.yellow('Type')]);
  if (tabs.length != 0) {
    for (var i = 0; i < tabs.length; i++) {
      var tab = tabs[i]
      table.push([colors.red(i.toString()), tab.artist, tab.name, tab.rating, tab.type])
    }
    console.log(table.toString());

  } else {
    console.log("No Results");
  }
}

function getTabs(name, pg) {
  return new Promise(function(resolve, reject) {
    ugs.search({
      query: name,
      page: pg,
      type: ['Tab', 'Chords']
    }, (error, tabs) => {
      if (error) {
        console.log(error)
        reject(err);
      } else {
        resolve(tabs);
      }
    })
  })
}


function getTab(tabUrl) {
console.log(tabUrl);
  ugs.get(tabUrl, (error, tab) => {
    if (error) {
      console.log(error)
    } else {
      var tab = tab.content.text
      tab = tab.replace(/\[ch\]/g, '').replace(/\[\/ch\]/g, '');
      console.log(tab);
    }
  })

}

function searchTab(name) {
  getTabs(name, 1).then(function(tabs) {
    listTabs(tabs)

    var schema = {
      properties: {
        ID: {
          description: 'Enter the ID of the Tab',
          pattern: /^\w+$/,
          required: true,
          type: "integer"
        }
      }
    };

    prompt.get("ID", function(err, result) {
        var tabUrl =  tabs[parseInt(result.ID)].url
        getTab(tabUrl)
    });

  }, function(err) {
    console.log(err);
  })
}


function init() {
  var schema = {
    properties: {
      search: {
        required: true,
        description: 'Enter the name of the artist or title of the tab',
        pattern: /^\w+$/
      }
    }
  };


  prompt.get(schema, function(err, result) {
    searchTab(result.search)
  });
}


init();
