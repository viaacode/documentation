FROM ruby:3.4-slim-trixie
RUN gem install bundler -v 2.6.9
WORKDIR /srv/jekyll
COPY Gemfile Gemfile.lock ./
RUN apt-get update && apt-get install -y --no-install-recommends build-essential git && rm -rf /var/lib/apt/lists/*
RUN bundle install
COPY . .
ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
