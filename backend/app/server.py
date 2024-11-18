# this is for our flask server.
from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
api = Api(app)

images = {0: {"fileName": "GOODBYE"}}
image_args = reqparse.RequestParser()
image_args.add_argument("fileName", type = str, help = "File location of image", required = True)

class Image(Resource):
    
    def get(self, img_id):
        if img_id not in images:
            abort(404, message = "Image id is not valid...")
        return images[img_id]
    
    def post(self, img_id):
        if img_id in images:
            abort(409, message = "Image already exists with ID")
        args = image_args.parse_args()
        images[img_id] = args
        return images[img_id], 201
    
    def delete(self,img_id):
        if img_id not in images:
            abort(404, message = "Image id is not valid...")
        del images[img_id]
        return '', 204
        
api.add_resource(Image, "/img/<int:img_id>")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)