from .third_party_youtube_lib import ThirdPartyYouTubeLib


class YouTubeManager:
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service

    def render_video_page(self, video_id: int) -> None:
        info = self.service.get_video_info(video_id)  # noqa
        # render video page

    def render_list_panel(self) -> None:
        video_list = self.service.list_videos()  # noqa
        # renders the list of video thumbnails

    def react_on_user_input(self, video_id: int) -> None:
        self.render_video_page(video_id)
        self.render_list_panel()
