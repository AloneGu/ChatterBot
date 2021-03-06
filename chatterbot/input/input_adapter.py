# encoding: utf-8
from __future__ import unicode_literals
from chatterbot.adapters import Adapter


class InputAdapter(Adapter):
    """
    This is an abstract class that represents the
    interface that all input adapters should implement.
    """

    def process_input(self, *args, **kwargs):
        """
        Returns a statement object based on the input source.
        """
        raise self.AdapterMethodNotImplementedError()

    def process_input_statement(self, *args, **kwargs):
        """
        Return an existing statement object (if one exists).
        """
        input_statement = self.process_input(*args, **kwargs)
        self.logger.info('Recieved input statement: {}'.format(input_statement.text))

        existing_statement = self.chatbot.storage.find(input_statement.text)

        if existing_statement:
            self.logger.info('"{}" is a known statement'.format(input_statement.text))
            input_statement = existing_statement
        else:
            self.logger.info('"{}" is not a known statement'.format(input_statement.text))

        return input_statement
