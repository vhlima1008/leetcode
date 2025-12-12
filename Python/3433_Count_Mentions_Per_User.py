"""
LeetCode: 3433 - Count Mentions Per User
Approach: Sort events by time/message priority, track offline back times, and process tokens per message to update mention counts.
Time: O(E * U) in worst case when messages use ALL/HERE across users; Space: O(U) for counters and back times.
"""

from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        back = [0] * numberOfUsers
        events.sort(key = lambda e: (int(e[1]), e[0]=="MESSAGE"))

        for responseType, time, data in events:
            time = int(time)
            if responseType == "OFFLINE":
                back[int(data)] = time + 60
                continue

            for token in data.split():
                if token == "ALL":
                    for user in range(numberOfUsers):
                        mentions[user] += 1
                elif token == "HERE":
                    for user in range(numberOfUsers):
                        if time >= back[user]:
                            mentions[user] += 1
                else:  
                    mentions[int(token[2:])] += 1

        return mentions
