const makeConfig = require('sc-recipe-staticresources');


module.exports = makeConfig(
  //name
  'cmcuritiba.portalmodelo.theme',

  //shortName
  'cmcuritibatema',

  //path
  `${__dirname}/../src/cmcuritiba/portalmodelo/theme`,

  //publicPath
  '++theme++cmcuritibatema/',

  //callback
  function(config, options) {
  },
);