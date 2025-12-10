FROM jekyll/jekyll:4.2.2
RUN gem install bundler -v 2.6.9
WORKDIR /srv/jekyll
COPY --chown=jekyll:jekyll Gemfile Gemfile.lock ./
RUN bundle install
COPY --chown=jekyll:jekyll . .
ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
