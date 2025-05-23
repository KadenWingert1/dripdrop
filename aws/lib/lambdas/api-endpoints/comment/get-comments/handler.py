import json
from utils import create_response, handle_exception
from sqlalchemy import select
from sqlalchemy_utils import session_handler
from dripdrop_orm_objects import Post

def handler(event, context):    
    try:
        # Get post ID from path parameters
        post_id = event['pathParameters'].get('post-id')

        if not post_id:
            return create_response(400, 'Missing required parameter: post id')
        
        # Call function to fetch comments
        status_code, data = getCommentsForPost(post_id)

        return create_response(status_code, data)
    
    except Exception as e:
        print(f"Error: {e}")
        return create_response(500, f"Error retrieving comments: {str(e)}")


@session_handler
def getCommentsForPost(session, post_id):
    try:
        # Fetch the post and its comments
        post = session.execute(
            select(Post).where(Post.postID == post_id)
        ).scalars().first()

        if not post:
            return 404, "Post not found."

        comments = post.comments or []

        if not comments:
            return 200, "No comments found for this post."

        comments_list = [
            {
                "commentID": comment.commentID,
                "username": comment.user.username,
                "profilePic": comment.user.profilePicURL,
                "content": comment.content,
                "createdDate": comment.createdDate.isoformat()
            }
            for comment in comments
        ]

        return 200, comments_list

    except Exception as e:
        return handle_exception(e, "Error accessing database")
