FROM jekyll/jekyll:4.2.2
RUN gem install bundler -v 2.6.9
WORKDIR /srv/jekyll
COPY Gemfile Gemfile.lock ./
RUN bundle install
COPY . .
ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
