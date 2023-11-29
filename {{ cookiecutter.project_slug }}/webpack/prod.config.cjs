const { merge } = require("webpack-merge");
const commonConfig = require("./common.config.cjs");

module.exports = merge(commonConfig, {
  mode: "production",
  output: {
    publicPath: "/static/",
  },
});
