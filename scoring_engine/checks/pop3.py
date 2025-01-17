from scoring_engine.engine.basic_check import BasicCheck


class POP3Check(BasicCheck):
    #required_properties = ['domain']
    CMD = "medusa -R 1 -h {0} -n {1} -u {2} -p {3} -M pop3"

    def command_format(self, properties):
        account = self.get_random_account()
        username_with_domain = account.username #+ '@' + properties['domain']
        return (self.host, self.port, username_with_domain, account.password)
