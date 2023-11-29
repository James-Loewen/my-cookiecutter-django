const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  target: "web",
  entry: [
    path.resolve(__dirname, "../assets/scripts/main.ts"),
    path.resolve(__dirname, "../assets/styles/main.css"),
  ],
  output: {
    filename: "[name]-[contenthash].js",
    path: path.resolve(__dirname, "../assets/build"),
    clean: true,
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name]-[contenthash].css",
    }),
    new BundleTracker({
      path: path.resolve(__dirname, "../"),
      filename: "webpack-stats.json",
    }),
  ],
  resolve: {
    extensions: [".ts", ".js"],
  },
  module: {
    rules: [
      {
        test: /\.ts$/i,
        use: "ts-loader",
        exclude: "/node_modules/",
      },
      {
        test: /\.css$/i,
        use: [MiniCssExtractPlugin.loader, "css-loader", "postcss-loader"],
      },
    ],
  },
};
