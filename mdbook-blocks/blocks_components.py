import re

'''

Alert component

'''

class BlocksAlert:

    def create_component(self):

        html = '''
        
        <div class="alert alert-primary my-5" role="alert">
            ''' + self.get('content') + '''
        </div>

        '''

        # Get all occurrences where there is two or more spaces within the text
        spaces = re.sub('[ ]{2,}', '', html)

        # Strip the string of "\n" and leading and trailing whitespace
        html = spaces.replace('\n', '').lstrip().rstrip()

        return html

'''

Card component

'''

class BlocksCard:

    def create_component(self):

        # Construct the HTML for a card
        if self.get('align') == 'True':

            html = '''

            <aligned>
            <div class="col-sm-3 my-4 d-flex align-items-stretch">
                <div class="card">
                    <img src="''' + self.get('image') + '''" class="card-img-top" alt="...">
                    <div class="card-body d-flex flex-column">
                        <p class="card-title">''' + self.get('title') + '''</p>
                        <p class="card-text">''' + self.get('caption') + '''</p>
                        <a href="''' + self.get('link') + '''" class="btn btn-primary mt-auto align-self-start">''' + self.get('button') + '''</a>
                    </div>
                </div>
            </div>

            '''

        else:

            html = '''

            <div class="row">
                <div class="col-sm-3 my-4">
                    <div class="card">
                        <img src="''' + self.get('image') + '''" class="card-img-top" alt="...">
                        <div class="card-body">
                            <p class="card-title">''' + self.get('title') + '''</p>
                            <p class="card-text">''' + self.get('caption') + '''</p>
                            <a href="''' + self.get('link') + '''" class="btn btn-primary">''' + self.get('button') + '''</a>
                        </div>
                    </div>
                </div>
            </div>

            '''

        # Get all occurrences where there is two or more spaces within the text
        spaces = re.sub('[ ]{2,}', '', html)

        # Strip the string of "\n" and leading and trailing whitespace
        html = spaces.replace('\n', '').lstrip().rstrip()

        return html

'''

Badge component

'''

class BlocksBadge:

    def create_component(self):

        # Construct the HTML for a badge
        html = '''
        
        <h1>''' + self.get('title') + ''' <span class="badge badge-primary">''' + self.get('content') + '''</span></h1>

        '''

        # Get all occurrences where there is two or more spaces within the text
        spaces = re.sub('[ ]{2,}', '', html)

        # Strip the string of "\n" and leading and trailing whitespace
        html = spaces.replace('\n', '').lstrip().rstrip()

        return html

'''

Button component

'''

class BlocksButton:

    def create_component(self):

        # Construct the HTML for a button
        if self.get('align') == 'True':

            # Construct the HTML for a button
            html = '''
            
            <aligned>
            <p>
                <a class="btn btn-primary my-2 mx-4" href="''' + self.get('link') + '''" role="button">''' + self.get('content') + '''</a>
            </p>

            '''

        else:

            # Construct the HTML for a button
            html = '''

            <a class="btn btn-primary my-2" href="''' + self.get('link') + '''" role="button">''' + self.get('content') + '''</a>

            '''

        # Get all occurrences where there is two or more spaces within the text
        spaces = re.sub('[ ]{2,}', '', html)

        # Strip the string of "\n" and leading and trailing whitespace
        html = spaces.replace('\n', '').lstrip().rstrip()

        return html