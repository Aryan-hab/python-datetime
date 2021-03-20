def time_ago(self):
        now = datetime.datetime.now()

        delta = now - self.publish # where publish is the time the comment is published on

        format_delta = delta.total_seconds() # calculating total seconds since the comment was posted

        # converting seconds to years, months, days, hours and minutes :

        years = format_delta // (60 * 60 * 24 * 30 * 12)

        months = format_delta // (60 * 60 * 24 * 30)

        days = format_delta // (60 * 60 * 24) 

        hours = format_delta // (60 * 60)

        minutes = format_delta // 60

        seconds = format_delta
        
        if seconds > 60:
            while months > 11.99:
                months -= 12

            while days > 29.99:
                days -= 30

            while hours > 23.99:
                hours -= 24

            while minutes > 59.99:
                minutes -= 60

            while seconds > 59.99:
                seconds -= 60

            date = ''
            if years > 0:
                if years == 1:
                    date += int(years) + ' year'
                else:
                    date += int(years) + ' years'
            if months > 0:
                if months == 1:
                    date += ' , ' + str(int(months)) + ' month'
                else:
                    date += ' , ' + str(int(months)) + ' months'
            if days > 0:
                if days == 1:
                    date += ' , ' + str(int(days))  + ' day'
                else:
                    date += ' , ' + str(int(days))  + ' days'
            if hours > 0:
                if hours == 1:
                    date += ' , ' + str(int(hours)) + ' hour'
                else:
                    date += ' , ' + str(int(hours)) + ' hours'
            if minutes > 0:
                date += ' , ' + str(int(minutes)) + ' minutes'

            date += ' ago'
            if years == 0:
                date = date[3:]
            return date
        else:
            return 'moments ago' # so that if the comment is posted less than a minute ago it will return 'moments ago'
