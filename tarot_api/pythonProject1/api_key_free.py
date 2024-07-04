from datetime import datetime, timedelta


class api_key_free:
    def __init__(self, api_key):
        self.free_key = api_key
        self.remaining_RPD = [14400, 14400, 14400, 14400]
        self.remaining_TPM = [15000, 6000, 30000, 5000]
        self.usage_RPM = [0, 0, 0, 0]
        tim_now = datetime.now()
        self.recovery_time = [tim_now, tim_now, tim_now, tim_now]

    def get_key(self):
        return self.free_key

    def increment_usage(self, requests=1, model=0):
        if datetime.now() - self.recovery_time[model] > timedelta(minutes=1):
            self.usage_RPM[model] = 0
            self.recovery_time[model] = datetime.now()
        self.usage_RPM[model] += requests
        if self.usage_RPM[model] > 25:
            self.usage_RPM[model] = 0
            self.recovery_time[model] = datetime.now() + timedelta(minutes=1)
        if self.remaining_TPM[model] < 400:
            self.remaining_TPM[model] = 5000
            self.recovery_time[model] = datetime.now() + timedelta(minutes=1)
        if self.remaining_RPD[model] < 400:
            self.remaining_RPD[model] = 14400
            self.usage_RPM[model] = 0
            self.recovery_time[model] = datetime.now() + timedelta(hours=1)

    def update_limits(self, headers, model=0):
        # print(f"RPM model {model}: {self.usage_RPM[model]}")
        if 'x-ratelimit-remaining-requests' in headers:
            self.remaining_RPD[model] = int(headers['x-ratelimit-remaining-requests'])
        if 'x-ratelimit-remaining-tokens' in headers:
            self.remaining_TPM[model] = int(headers['x-ratelimit-remaining-tokens'])

    def is_available(self, model):
        if (self.remaining_RPD[model] > 0 and
                self.remaining_TPM[model] > 1024 and
                datetime.now() > self.recovery_time[model]):
            return True
        return False
