const path = require('path')
			module.exports = {
				mode : "development",
				entry : './src/index.js',
				output: {
					filename : 'bundle.js',
					path: path.resolve(__dirname, '../backend/static/js')
				},
				module:{
					rules: [
						{
							test : /\.js$/,
							exclude : /node_modules/,
							use : {
								loader: "babel-loader"
							}
						}
					]
				},
				
				devtool: "source-map",

				devServer: {
					contentBase: './public_html'
				}
			}