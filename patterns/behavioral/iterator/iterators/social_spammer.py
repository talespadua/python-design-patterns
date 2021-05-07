from patterns.behavioral.iterator.iterators.profile_iterator import ProfileIterator


class SocialSpammer:
    def send(self, iterator: ProfileIterator, message: str) -> None:
        while iterator.has_more():
            profile = iterator.get_next()
            if profile:
                self.send_mail(profile.email, message)

    def send_mail(self, email: str, message: str) -> None:
        return None
