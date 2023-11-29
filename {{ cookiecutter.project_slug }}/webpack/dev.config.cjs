const { merge } = require("webpack-merge");
const commonConfig = require("./common.config.cjs");

module.exports = merge(commonConfig, {
  mode: "development",
  devtool: "inline-source-map",
  watchOptions: {
    ignored: "/node_modules",
    aggregateTimeout: 50,
    poll: 1000,
  },
});
