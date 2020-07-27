class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.checkipv4(IP)
        elif IP.count(':') == 7:
            return self.checkipv6(IP)
        else:
            return 'Neither'
        
    def checkipv4(self, IP):
        parts = IP.split('.')
        for num in parts:
            if len(num) == 0 or len(num) > 3:
                return 'Neither'
            if not num.isdigit() or (num[0] == '0' and len(num) != 1) or int(num) < 0 or int(num) > 255:
                return 'Neither'
        return 'IPv4'
            
    def checkipv6(self, IP):
        parts = IP.split(':')
        hexnums = '0123456789abcdefABCDEF'
        
        for num in parts:
            if len(num) == 0 or len(num) > 4 or not all(c in hexnums for c in num):
                return 'Neither'
        return 'IPv6'