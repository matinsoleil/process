import falcon
import ZODB, ZODB.FileStorage

class URL(object):
	def on_get(self, req, res):
		res.status = falcon.HTTP_200
		res.body = ('can you see tas every')


class TestResource(object):
    def on_get(self, req, res):
        """Handles all GET requests."""
        res.status = falcon.HTTP_200  # This is the default status
        res.body = ('This is me, Falcon, serving a resource!')

# Create the Falcon application object
app = falcon.API()

# Instantiate the TestResource class
test_resource = TestResource()

ok = URL()

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)

# Add a route to serve the resource
app.add_route('/test', test_resource)
app.add_route('/status',ok)
