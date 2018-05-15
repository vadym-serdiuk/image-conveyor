from flask_restplus import Api

api = Api(version='0.1', title='Photo processing',
          description='Convert images by applying canny edge detection filter')