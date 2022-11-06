class Solution:
    def realEmail(self, email: str) -> int:
        i = email.index('@')
        return email[:i].split('+', 1)[0].replace('.', '') + email[i:]

    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            seen.add(self.realEmail(email))
        return len(seen)
