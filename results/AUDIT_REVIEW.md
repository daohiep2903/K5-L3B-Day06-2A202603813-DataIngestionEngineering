# Hồ sơ đánh giá chất lượng dữ liệu và truy xuất

**Học viên, tác giả bài làm: Đào Văn Hiệp — 2A202603813 — L3B.**

**Có sử dụng AI hỗ trợ đánh giá.** Phần định tính do AI đọc nội dung; metadata được đối chiếu bằng chương trình. Các chỉ số retrieval gốc được giữ nguyên.

## Tổng hợp

| Cấu hình | Mạch lạc chunk /2 (10 mẫu) | Đủ bằng chứng /2 (5 câu) | Metadata khớp nguồn | Top-3 đúng phạm vi filter |
|---|---:|---:|---:|---:|
| A | 1,4 | 2,0 | 15/15 | 0/2 |
| B | 1,9 | 2,0 | 15/15 | 1/2 |
| C | 1,9 | 2,0 | 15/15 | 2/2 |

## Tính mạch lạc của chunk: cùng 10 vị trí nguồn cho mỗi cấu hình

Thang điểm: **0** = khó hiểu vì bị cắt ý hoặc thiếu chủ thể; **1** = hiểu được một phần nhưng thiếu ngữ cảnh; **2** = đủ ngữ cảnh và giữ trọn ý để hiểu. Chấm toàn bộ chunk mẫu, không chỉ câu đầu. Mười đơn vị nguồn đầu được chọn trước khi chấm retrieval; cách lấy mẫu này thiên về phần đầu tài liệu.

### A / rfc6749-unit-001
**Điểm: 1/2.** Lý do: Phần đăng ký client có thể hiểu được, nhưng đoạn tiếp theo bị cắt giữa từ.
Đơn vị nguồn 1; mục 2; khoảng ký tự [0, 500); ID chunk `f01ddafe1e197acfb6d74c1a4394355ad1e5c7ef77280fe0a8df9cd84d57f837`.

```text
2.  Client Registration

   Before initiating the protocol, the client registers with the
   authorization server.  The means through which the client registers
   with the authorization server are beyond the scope of this
   specification but typically involve end-user interaction with an HTML
   registration form.

   Client registration does not require a direct interaction between the
   client and the authorization server.  When supported by the
   authorization server, registration can rel
```

### B / rfc6749-unit-001
**Điểm: 1/2.** Lý do: Các đoạn về đăng ký client đầy đủ, nhưng danh sách SHALL chỉ có yêu cầu đầu tiên; các yêu cầu còn lại nằm ở chunk sau.
Đơn vị nguồn 1; mục 2; khoảng ký tự [0, 940); ID chunk `417f88f04302b2a322519149f0c5453119ff54f71596b1029fc0a01cf7454be0`.

```text
2.  Client Registration

   Before initiating the protocol, the client registers with the
   authorization server.  The means through which the client registers
   with the authorization server are beyond the scope of this
   specification but typically involve end-user interaction with an HTML
   registration form.

   Client registration does not require a direct interaction between the
   client and the authorization server.  When supported by the
   authorization server, registration can rely on other means for
   establishing trust and obtaining the required client properties
   (e.g., redirection URI, client type).  For example, registration can
   be accomplished using a self-issued or third-party-issued assertion,
   or by the authorization server performing client discovery using a
   trusted channel.

   When registering a client, the client developer SHALL:

   o  specify the client type as described in Section 2.1,
```

### C / rfc6749-unit-001
**Điểm: 1/2.** Lý do: Các đoạn về đăng ký client đầy đủ, nhưng danh sách SHALL chỉ có yêu cầu đầu tiên; các yêu cầu còn lại nằm ở chunk sau.
Đơn vị nguồn 1; mục 2; khoảng ký tự [0, 940); ID chunk `417f88f04302b2a322519149f0c5453119ff54f71596b1029fc0a01cf7454be0`.

```text
2.  Client Registration

   Before initiating the protocol, the client registers with the
   authorization server.  The means through which the client registers
   with the authorization server are beyond the scope of this
   specification but typically involve end-user interaction with an HTML
   registration form.

   Client registration does not require a direct interaction between the
   client and the authorization server.  When supported by the
   authorization server, registration can rely on other means for
   establishing trust and obtaining the required client properties
   (e.g., redirection URI, client type).  For example, registration can
   be accomplished using a self-issued or third-party-issued assertion,
   or by the authorization server performing client discovery using a
   trusted channel.

   When registering a client, the client developer SHALL:

   o  specify the client type as described in Section 2.1,
```

### A / rfc6749-unit-002
**Điểm: 1/2.** Lý do: Định nghĩa public client đầy đủ, nhưng đoạn sau bị cắt.
Đơn vị nguồn 2; mục 2; khoảng ký tự [1694, 2191); ID chunk `3f56b4014bf69c7d9fafb5dc7e99f974b2463da119a2926a3f96c52fd8cc34f2`.

```text
public
      Clients incapable of maintaining the confidentiality of their
      credentials (e.g., clients executing on the device used by the
      resource owner, such as an installed native application or a web
      browser-based application), and incapable of secure client
      authentication via any other means.

   The client type designation is based on the authorization server's
   definition of secure authentication and its acceptable exposure
   levels of client credentials.  The
```

### B / rfc6749-unit-002
**Điểm: 2/2.** Lý do: Định nghĩa public client và lưu ý về cách xác định loại client đều đầy đủ.
Đơn vị nguồn 2; mục 2; khoảng ký tự [1694, 2266); ID chunk `d0a76a6fd624f8e731baeaea9751231f1ca54d2fb540d3a359550335b18cf4e4`.

```text
public
      Clients incapable of maintaining the confidentiality of their
      credentials (e.g., clients executing on the device used by the
      resource owner, such as an installed native application or a web
      browser-based application), and incapable of secure client
      authentication via any other means.

   The client type designation is based on the authorization server's
   definition of secure authentication and its acceptable exposure
   levels of client credentials.  The authorization server SHOULD NOT
   make assumptions about the client type.
```

### C / rfc6749-unit-002
**Điểm: 2/2.** Lý do: Định nghĩa public client và lưu ý về cách xác định loại client đều đầy đủ.
Đơn vị nguồn 2; mục 2; khoảng ký tự [1694, 2266); ID chunk `d0a76a6fd624f8e731baeaea9751231f1ca54d2fb540d3a359550335b18cf4e4`.

```text
public
      Clients incapable of maintaining the confidentiality of their
      credentials (e.g., clients executing on the device used by the
      resource owner, such as an installed native application or a web
      browser-based application), and incapable of secure client
      authentication via any other means.

   The client type designation is based on the authorization server's
   definition of secure authentication and its acceptable exposure
   levels of client credentials.  The authorization server SHOULD NOT
   make assumptions about the client type.
```

### A / rfc6749-unit-003
**Điểm: 1/2.** Lý do: Định nghĩa ứng dụng chạy trên trình duyệt bị cắt giữa câu.
Đơn vị nguồn 3; mục 2; khoảng ký tự [3223, 3720); ID chunk `d7019b39269a3e1c90b839c7dc1ae28c90ecd19313c4cf70e6a87c6278499363`.

```text
user-agent-based application
      A user-agent-based application is a public client in which the
      client code is downloaded from a web server and executes within a
      user-agent (e.g., web browser) on the device used by the resource
      owner.  Protocol data and credentials are easily accessible (and
      often visible) to the resource owner.  Since such applications
      reside within the user-agent, they can make seamless use of the
      user-agent capabilities when requesting
```

### B / rfc6749-unit-003
**Điểm: 2/2.** Lý do: Định nghĩa ứng dụng chạy trên trình duyệt đầy đủ và có ngữ cảnh hữu ích.
Đơn vị nguồn 3; mục 2; khoảng ký tự [3223, 3735); ID chunk `eeb280a89564631821610936ff86d03caa773849cb60da87693aaab304b97044`.

```text
user-agent-based application
      A user-agent-based application is a public client in which the
      client code is downloaded from a web server and executes within a
      user-agent (e.g., web browser) on the device used by the resource
      owner.  Protocol data and credentials are easily accessible (and
      often visible) to the resource owner.  Since such applications
      reside within the user-agent, they can make seamless use of the
      user-agent capabilities when requesting authorization.
```

### C / rfc6749-unit-003
**Điểm: 2/2.** Lý do: Định nghĩa ứng dụng chạy trên trình duyệt đầy đủ và có ngữ cảnh hữu ích.
Đơn vị nguồn 3; mục 2; khoảng ký tự [3223, 3735); ID chunk `eeb280a89564631821610936ff86d03caa773849cb60da87693aaab304b97044`.

```text
user-agent-based application
      A user-agent-based application is a public client in which the
      client code is downloaded from a web server and executes within a
      user-agent (e.g., web browser) on the device used by the resource
      owner.  Protocol data and credentials are easily accessible (and
      often visible) to the resource owner.  Since such applications
      reside within the user-agent, they can make seamless use of the
      user-agent capabilities when requesting authorization.
```

### A / rfc6749-unit-004
**Điểm: 2/2.** Lý do: Đoạn văn đầy đủ, nêu rõ không được giả định độ dài client identifier.
Đơn vị nguồn 4; mục 2; khoảng ký tự [4859, 5093); ID chunk `25c30c4ff7d19bdc7748f63ba7d5eb6d9e93ecd65a86e255bbc23327fe17e6ef`.

```text
The client identifier string size is left undefined by this
   specification.  The client should avoid making assumptions about the
   identifier size.  The authorization server SHOULD document the size
   of any identifier it issues.
```

### B / rfc6749-unit-004
**Điểm: 2/2.** Lý do: Đoạn văn về độ dài client identifier đầy đủ.
Đơn vị nguồn 4; mục 2; khoảng ký tự [4859, 5093); ID chunk `25c30c4ff7d19bdc7748f63ba7d5eb6d9e93ecd65a86e255bbc23327fe17e6ef`.

```text
The client identifier string size is left undefined by this
   specification.  The client should avoid making assumptions about the
   identifier size.  The authorization server SHOULD document the size
   of any identifier it issues.
```

### C / rfc6749-unit-004
**Điểm: 2/2.** Lý do: Đoạn văn về độ dài client identifier đầy đủ.
Đơn vị nguồn 4; mục 2; khoảng ký tự [4859, 5093); ID chunk `25c30c4ff7d19bdc7748f63ba7d5eb6d9e93ecd65a86e255bbc23327fe17e6ef`.

```text
The client identifier string size is left undefined by this
   specification.  The client should avoid making assumptions about the
   identifier size.  The authorization server SHOULD document the size
   of any identifier it issues.
```

### A / rfc6749-unit-005
**Điểm: 1/2.** Lý do: Định nghĩa client_secret bị cắt giữa từ, làm mất ngoại lệ khi secret là chuỗi rỗng.
Đơn vị nguồn 5; mục 2; khoảng ký tự [6529, 7026); ID chunk `ee2fc13db7a2755a53de9030e1c28a457870639af3b3ccb3985107861d113051`.

```text
For example (with extra line breaks for display purposes only):

     Authorization: Basic czZCaGRSa3F0Mzo3RmpmcDBaQnIxS3REUmJuZlZkbUl3

   Alternatively, the authorization server MAY support including the
   client credentials in the request-body using the following
   parameters:

   client_id
         REQUIRED.  The client identifier issued to the client during
         the registration process described by Section 2.2.

   client_secret
         REQUIRED.  The client secret.  The client M
```

### B / rfc6749-unit-005
**Điểm: 2/2.** Lý do: Giữ đủ tham số credential trong body, ngoại lệ secret rỗng và hạn chế không đưa vào URI. Ví dụ Basic ở đầu cần ngữ cảnh trước đó, nhưng nội dung chính vẫn hiểu được.
Đơn vị nguồn 5; mục 2; khoảng ký tự [6529, 7470); ID chunk `742b33add5702a33de11ebb7a3daab29f9e2f4158095dd6c8c62b01dab7e8ff2`.

```text
For example (with extra line breaks for display purposes only):

     Authorization: Basic czZCaGRSa3F0Mzo3RmpmcDBaQnIxS3REUmJuZlZkbUl3

   Alternatively, the authorization server MAY support including the
   client credentials in the request-body using the following
   parameters:

   client_id
         REQUIRED.  The client identifier issued to the client during
         the registration process described by Section 2.2.

   client_secret
         REQUIRED.  The client secret.  The client MAY omit the
         parameter if the client secret is an empty string.

   Including the client credentials in the request-body using the two
   parameters is NOT RECOMMENDED and SHOULD be limited to clients unable
   to directly utilize the HTTP Basic authentication scheme (or other
   password-based HTTP authentication schemes).  The parameters can only
   be transmitted in the request-body and MUST NOT be included in the
   request URI.
```

### C / rfc6749-unit-005
**Điểm: 2/2.** Lý do: Giữ đủ tham số credential trong body, ngoại lệ secret rỗng và hạn chế không đưa vào URI. Ví dụ Basic ở đầu cần ngữ cảnh trước đó, nhưng nội dung chính vẫn hiểu được.
Đơn vị nguồn 5; mục 2; khoảng ký tự [6529, 7470); ID chunk `742b33add5702a33de11ebb7a3daab29f9e2f4158095dd6c8c62b01dab7e8ff2`.

```text
For example (with extra line breaks for display purposes only):

     Authorization: Basic czZCaGRSa3F0Mzo3RmpmcDBaQnIxS3REUmJuZlZkbUl3

   Alternatively, the authorization server MAY support including the
   client credentials in the request-body using the following
   parameters:

   client_id
         REQUIRED.  The client identifier issued to the client during
         the registration process described by Section 2.2.

   client_secret
         REQUIRED.  The client secret.  The client MAY omit the
         parameter if the client secret is an empty string.

   Including the client credentials in the request-body using the two
   parameters is NOT RECOMMENDED and SHOULD be limited to clients unable
   to directly utilize the HTTP Basic authentication scheme (or other
   password-based HTTP authentication schemes).  The parameters can only
   be transmitted in the request-body and MUST NOT be included in the
   request URI.
```

### A / rfc6749-unit-006
**Điểm: 2/2.** Lý do: Có tiêu đề và đoạn văn đầy đủ giải thích ánh xạ phương thức xác thực với client identifier.
Đơn vị nguồn 6; mục 2; khoảng ký tự [8169, 8502); ID chunk `b8f7a293ed6092090239af3ea40cbd7c5f25df0b82ebd4033fc4c360012dd687`.

```text
2.3.2.  Other Authentication Methods

   The authorization server MAY support any suitable HTTP authentication
   scheme matching its security requirements.  When using other
   authentication methods, the authorization server MUST define a
   mapping between the client identifier (registration record) and
   authentication scheme.
```

### B / rfc6749-unit-006
**Điểm: 2/2.** Lý do: Có tiêu đề và đoạn văn đầy đủ về ánh xạ phương thức xác thực.
Đơn vị nguồn 6; mục 2; khoảng ký tự [8169, 8502); ID chunk `b8f7a293ed6092090239af3ea40cbd7c5f25df0b82ebd4033fc4c360012dd687`.

```text
2.3.2.  Other Authentication Methods

   The authorization server MAY support any suitable HTTP authentication
   scheme matching its security requirements.  When using other
   authentication methods, the authorization server MUST define a
   mapping between the client identifier (registration record) and
   authentication scheme.
```

### C / rfc6749-unit-006
**Điểm: 2/2.** Lý do: Có tiêu đề và đoạn văn đầy đủ về ánh xạ phương thức xác thực.
Đơn vị nguồn 6; mục 2; khoảng ký tự [8169, 8502); ID chunk `b8f7a293ed6092090239af3ea40cbd7c5f25df0b82ebd4033fc4c360012dd687`.

```text
2.3.2.  Other Authentication Methods

   The authorization server MAY support any suitable HTTP authentication
   scheme matching its security requirements.  When using other
   authentication methods, the authorization server MUST define a
   mapping between the client identifier (registration record) and
   authentication scheme.
```

### A / rfc6749-unit-007
**Điểm: 1/2.** Lý do: Quy định về URI đầy đủ, nhưng phần nói về TLS vừa bắt đầu đã bị cắt.
Đơn vị nguồn 7; mục 3; khoảng ký tự [9928, 10424); ID chunk `58107d76a01b0b7ffdb6b8157df1f4bfe9b139c43b855897d6afb34ee7a78b6a`.

```text
The means through which the client obtains the location of the
   authorization endpoint are beyond the scope of this specification,
   but the location is typically provided in the service documentation.

   The endpoint URI MAY include an "application/x-www-form-urlencoded"
   formatted (per Appendix B) query component ([RFC3986] Section 3.4),
   which MUST be retained when adding additional query parameters.  The
   endpoint URI MUST NOT include a fragment component.

   Since requests to
```

### B / rfc6749-unit-007
**Điểm: 2/2.** Lý do: Giữ đủ quy định về vị trí endpoint, fragment, TLS và phương thức HTTP.
Đơn vị nguồn 7; mục 3; khoảng ký tự [9928, 10874); ID chunk `4a5d1d2a0e18d68970182108d993a20fe5a0998aeffe89df150f8f1634a9be0a`.

```text
The means through which the client obtains the location of the
   authorization endpoint are beyond the scope of this specification,
   but the location is typically provided in the service documentation.

   The endpoint URI MAY include an "application/x-www-form-urlencoded"
   formatted (per Appendix B) query component ([RFC3986] Section 3.4),
   which MUST be retained when adding additional query parameters.  The
   endpoint URI MUST NOT include a fragment component.

   Since requests to the authorization endpoint result in user
   authentication and the transmission of clear-text credentials (in the
   HTTP response), the authorization server MUST require the use of TLS
   as described in Section 1.6 when sending requests to the
   authorization endpoint.

   The authorization server MUST support the use of the HTTP "GET"
   method [RFC2616] for the authorization endpoint and MAY support the
   use of the "POST" method as well.
```

### C / rfc6749-unit-007
**Điểm: 2/2.** Lý do: Giữ đủ quy định về vị trí endpoint, fragment, TLS và phương thức HTTP.
Đơn vị nguồn 7; mục 3; khoảng ký tự [9928, 10874); ID chunk `4a5d1d2a0e18d68970182108d993a20fe5a0998aeffe89df150f8f1634a9be0a`.

```text
The means through which the client obtains the location of the
   authorization endpoint are beyond the scope of this specification,
   but the location is typically provided in the service documentation.

   The endpoint URI MAY include an "application/x-www-form-urlencoded"
   formatted (per Appendix B) query component ([RFC3986] Section 3.4),
   which MUST be retained when adding additional query parameters.  The
   endpoint URI MUST NOT include a fragment component.

   Since requests to the authorization endpoint result in user
   authentication and the transmission of clear-text credentials (in the
   HTTP response), the authorization server MUST require the use of TLS
   as described in Section 1.6 when sending requests to the
   authorization endpoint.

   The authorization server MUST support the use of the HTTP "GET"
   method [RFC2616] for the authorization endpoint and MAY support the
   use of the "POST" method as well.
```

### A / rfc6749-unit-008
**Điểm: 2/2.** Lý do: Hai đoạn văn đầy đủ mô tả response type kết hợp và cách xử lý lỗi.
Đơn vị nguồn 8; mục 3; khoảng ký tự [11686, 12168); ID chunk `0fdddc6810af51fd353ed142723293622ed997a4a1830f2986fe0208aca742c9`.

```text
Extension response types MAY contain a space-delimited (%x20) list of
   values, where the order of values does not matter (e.g., response
   type "a b" is the same as "b a").  The meaning of such composite
   response types is defined by their respective specifications.

   If an authorization request is missing the "response_type" parameter,
   or if the response type is not understood, the authorization server
   MUST return an error response as described in Section 4.1.2.1.
```

### B / rfc6749-unit-008
**Điểm: 2/2.** Lý do: Các đoạn về response type và lỗi đều đầy đủ.
Đơn vị nguồn 8; mục 3; khoảng ký tự [11686, 12168); ID chunk `0fdddc6810af51fd353ed142723293622ed997a4a1830f2986fe0208aca742c9`.

```text
Extension response types MAY contain a space-delimited (%x20) list of
   values, where the order of values does not matter (e.g., response
   type "a b" is the same as "b a").  The meaning of such composite
   response types is defined by their respective specifications.

   If an authorization request is missing the "response_type" parameter,
   or if the response type is not understood, the authorization server
   MUST return an error response as described in Section 4.1.2.1.
```

### C / rfc6749-unit-008
**Điểm: 2/2.** Lý do: Các đoạn về response type và lỗi đều đầy đủ.
Đơn vị nguồn 8; mục 3; khoảng ký tự [11686, 12168); ID chunk `0fdddc6810af51fd353ed142723293622ed997a4a1830f2986fe0208aca742c9`.

```text
Extension response types MAY contain a space-delimited (%x20) list of
   values, where the order of values does not matter (e.g., response
   type "a b" is the same as "b a").  The meaning of such composite
   response types is defined by their respective specifications.

   If an authorization request is missing the "response_type" parameter,
   or if the response type is not understood, the authorization server
   MUST return an error response as described in Section 4.1.2.1.
```

### A / rfc6749-unit-009
**Điểm: 2/2.** Lý do: Đoạn văn đầy đủ giải thích rủi ro khi thiếu bảo mật tầng truyền tải.
Đơn vị nguồn 9; mục 3; khoảng ký tự [13642, 13999); ID chunk `ff6febd05a1a919963db33c7afb3c85a574eefeb6029d3be19e3b073b3ab52d1`.

```text
Lack of transport-layer security can have a severe impact on the
   security of the client and the protected resources it is authorized
   to access.  The use of transport-layer security is particularly
   critical when the authorization process is used as a form of
   delegated end-user authentication by the client (e.g., third-party
   sign-in service).
```

### B / rfc6749-unit-009
**Điểm: 2/2.** Lý do: Giải thích đầy đủ rủi ro bảo mật tầng truyền tải.
Đơn vị nguồn 9; mục 3; khoảng ký tự [13642, 13999); ID chunk `ff6febd05a1a919963db33c7afb3c85a574eefeb6029d3be19e3b073b3ab52d1`.

```text
Lack of transport-layer security can have a severe impact on the
   security of the client and the protected resources it is authorized
   to access.  The use of transport-layer security is particularly
   critical when the authorization process is used as a form of
   delegated end-user authentication by the client (e.g., third-party
   sign-in service).
```

### C / rfc6749-unit-009
**Điểm: 2/2.** Lý do: Giải thích đầy đủ rủi ro bảo mật tầng truyền tải.
Đơn vị nguồn 9; mục 3; khoảng ký tự [13642, 13999); ID chunk `ff6febd05a1a919963db33c7afb3c85a574eefeb6029d3be19e3b073b3ab52d1`.

```text
Lack of transport-layer security can have a severe impact on the
   security of the client and the protected resources it is authorized
   to access.  The use of transport-layer security is particularly
   critical when the authorization process is used as a form of
   delegated end-user authentication by the client (e.g., third-party
   sign-in service).
```

### A / rfc6749-unit-010
**Điểm: 1/2.** Lý do: Quy định gửi redirect URI đầy đủ, nhưng quy định đối chiếu URI bị cắt giữa từ.
Đơn vị nguồn 10; mục 3; khoảng ký tự [15146, 15646); ID chunk `309189f57ba8f07e8cf930784d7483ae2ecbcf1dc494f10a0221ff8cfd44f428`.

```text
3.1.2.3.  Dynamic Configuration

   If multiple redirection URIs have been registered, if only part of
   the redirection URI has been registered, or if no redirection URI has
   been registered, the client MUST include a redirection URI with the
   authorization request using the "redirect_uri" request parameter.

   When a redirection URI is included in an authorization request, the
   authorization server MUST compare and match the value received
   against at least one of the registered redi
```

### B / rfc6749-unit-010
**Điểm: 2/2.** Lý do: Có tiêu đề và đầy đủ quy định gửi, đối chiếu redirect URI.
Đơn vị nguồn 10; mục 3; khoảng ký tự [15146, 15950); ID chunk `292a138063c447857a0393170ae056a1fc75f197d2c14877e4d63c32dc96bcc2`.

```text
3.1.2.3.  Dynamic Configuration

   If multiple redirection URIs have been registered, if only part of
   the redirection URI has been registered, or if no redirection URI has
   been registered, the client MUST include a redirection URI with the
   authorization request using the "redirect_uri" request parameter.

   When a redirection URI is included in an authorization request, the
   authorization server MUST compare and match the value received
   against at least one of the registered redirection URIs (or URI
   components) as defined in [RFC3986] Section 6, if any redirection
   URIs were registered.  If the client registration included the full
   redirection URI, the authorization server MUST compare the two URIs
   using simple string comparison as defined in [RFC3986] Section 6.2.1.
```

### C / rfc6749-unit-010
**Điểm: 2/2.** Lý do: Có tiêu đề và đầy đủ quy định gửi, đối chiếu redirect URI.
Đơn vị nguồn 10; mục 3; khoảng ký tự [15146, 15950); ID chunk `292a138063c447857a0393170ae056a1fc75f197d2c14877e4d63c32dc96bcc2`.

```text
3.1.2.3.  Dynamic Configuration

   If multiple redirection URIs have been registered, if only part of
   the redirection URI has been registered, or if no redirection URI has
   been registered, the client MUST include a redirection URI with the
   authorization request using the "redirect_uri" request parameter.

   When a redirection URI is included in an authorization request, the
   authorization server MUST compare and match the value received
   against at least one of the registered redirection URIs (or URI
   components) as defined in [RFC3986] Section 6, if any redirection
   URIs were registered.  If the client registration included the full
   redirection URI, the authorization server MUST compare the two URIs
   using simple string comparison as defined in [RFC3986] Section 6.2.1.
```

## Độ đủ bằng chứng và metadata: 5 câu test cho mỗi cấu hình

Thang điểm grounding: **0** = không có bằng chứng; **1** = có nhưng thiếu điều kiện hoặc ngữ cảnh cần thiết; **2** = đủ để trả lời và truy nguồn. Chấm cả tập top-3. Metadata được đối chiếu với text và vị trí nguồn thực tế. A/B là cấu hình không filter; tỷ lệ đúng phạm vi của chúng chỉ để so sánh, không phải lỗi thực thi filter.

### A / q16
**Câu hỏi:** Theo mục 2, client có thể giả định một độ dài cố định cho client identifier không?

**Đáp án dự kiến:** Không. Độ dài không được quy định; client nên tránh giả định về độ dài.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-1 nêu rõ độ dài identifier không được quy định và client nên tránh giả định về độ dài.
**Filter từ câu hỏi:** {"top_level_section": "2"}

**Hạng 1:** đơn vị nguồn 4, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [4859, 5093).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The client identifier string size is left undefined by this
   specification.  The client should avoid making assumptions about the
   identifier size.  The authorization server SHOULD document the size
   of any identifier it issues.
```

**Hạng 2:** đơn vị nguồn 3, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [4461, 4854).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
2.2.  Client Identifier

   The authorization server issues the registered client a client
   identifier -- a unique string representing the registration
   information provided by the client.  The client identifier is not a
   secret; it is exposed to the resource owner and MUST NOT be used
   alone for client authentication.  The client identifier is unique to
   the authorization server.
```

**Hạng 3:** đơn vị nguồn 18, mục 4, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [28973, 29211).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
eters.  The
   authorization code string size is left undefined by this
   specification.  The client should avoid making assumptions about code
   value sizes.  The authorization server SHOULD document the size of
   any value it issues.
```

### B / q16
**Câu hỏi:** Theo mục 2, client có thể giả định một độ dài cố định cho client identifier không?

**Đáp án dự kiến:** Không. Độ dài không được quy định; client nên tránh giả định về độ dài.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-1 nêu rõ độ dài identifier không được quy định và client nên tránh giả định về độ dài.
**Filter từ câu hỏi:** {"top_level_section": "2"}

**Hạng 1:** đơn vị nguồn 4, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [4859, 5093).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The client identifier string size is left undefined by this
   specification.  The client should avoid making assumptions about the
   identifier size.  The authorization server SHOULD document the size
   of any identifier it issues.
```

**Hạng 2:** đơn vị nguồn 3, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [4461, 4854).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
2.2.  Client Identifier

   The authorization server issues the registered client a client
   identifier -- a unique string representing the registration
   information provided by the client.  The client identifier is not a
   secret; it is exposed to the resource owner and MUST NOT be used
   alone for client authentication.  The client identifier is unique to
   the authorization server.
```

**Hạng 3:** đơn vị nguồn 6, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [8504, 8772).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
2.4.  Unregistered Clients

   This specification does not exclude the use of unregistered clients.
   However, the use of such clients is beyond the scope of this
   specification and requires additional security analysis and review of
   its interoperability impact.
```

### C / q16
**Câu hỏi:** Theo mục 2, client có thể giả định một độ dài cố định cho client identifier không?

**Đáp án dự kiến:** Không. Độ dài không được quy định; client nên tránh giả định về độ dài.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-1 nêu rõ độ dài identifier không được quy định và client nên tránh giả định về độ dài.
**Filter từ câu hỏi:** {"top_level_section": "2"}

**Hạng 1:** đơn vị nguồn 4, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [4859, 5093).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The client identifier string size is left undefined by this
   specification.  The client should avoid making assumptions about the
   identifier size.  The authorization server SHOULD document the size
   of any identifier it issues.
```

**Hạng 2:** đơn vị nguồn 3, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [4461, 4854).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
2.2.  Client Identifier

   The authorization server issues the registered client a client
   identifier -- a unique string representing the registration
   information provided by the client.  The client identifier is not a
   secret; it is exposed to the resource owner and MUST NOT be used
   alone for client authentication.  The client identifier is unique to
   the authorization server.
```

**Hạng 3:** đơn vị nguồn 6, mục 2, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [8504, 8772).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
2.4.  Unregistered Clients

   This specification does not exclude the use of unregistered clients.
   However, the use of such clients is beyond the scope of this
   specification and requires additional security analysis and review of
   its interoperability impact.
```

### A / q17
**Câu hỏi:** Một yêu cầu cấp quyền có được chứa cùng một tham số nhiều lần không?

**Đáp án dự kiến:** Không.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-1 nêu rõ tham số yêu cầu và phản hồi KHÔNG ĐƯỢC xuất hiện nhiều hơn một lần.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 7, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [10826, 11118).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
support the
   use of the "POST" method as well.

   Parameters sent without a value MUST be treated as if they were
   omitted from the request.  The authorization server MUST ignore
   unrecognized request parameters.  Request and response parameters
   MUST NOT be included more than once.
```

**Hạng 2:** đơn vị nguồn 9, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [14451, 14947).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
plete redirection URI (the client MAY use the "state" request
   parameter to achieve per-request customization).  If requiring the
   registration of the complete redirection URI is not possible, the
   authorization server SHOULD require the registration of the URI
   scheme, authority, and path (allowing the client to dynamically vary
   only the query component of the redirection URI when requesting
   authorization).

   The authorization server MAY allow the client to register multiple
```

**Hạng 3:** đơn vị nguồn 30, mục 4, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [49864, 50115).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
4.3.1.  Authorization Request and Response

   The method through which the client obtains the resource owner
   credentials is beyond the scope of this specification.  The client
   MUST discard the credentials once an access token has been obtained.
```

### B / q17
**Câu hỏi:** Một yêu cầu cấp quyền có được chứa cùng một tham số nhiều lần không?

**Đáp án dự kiến:** Không.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-1 nêu rõ tham số yêu cầu và phản hồi KHÔNG ĐƯỢC xuất hiện nhiều hơn một lần.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 7, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [10879, 11118).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
Parameters sent without a value MUST be treated as if they were
   omitted from the request.  The authorization server MUST ignore
   unrecognized request parameters.  Request and response parameters
   MUST NOT be included more than once.
```

**Hạng 2:** đơn vị nguồn 17, mục 4, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [28197, 28521).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
more than once.  If an authorization code is used more than
         once, the authorization server MUST deny the request and SHOULD
         revoke (when possible) all tokens previously issued based on
         that authorization code.  The authorization code is bound to
         the client identifier and redirection URI.
```

**Hạng 3:** đơn vị nguồn 13, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [21296, 21615).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
If the client omits the scope parameter when requesting
   authorization, the authorization server MUST either process the
   request using a pre-defined default value or fail the request
   indicating an invalid scope.  The authorization server SHOULD
   document its scope requirements and default value (if defined).
```

### C / q17
**Câu hỏi:** Một yêu cầu cấp quyền có được chứa cùng một tham số nhiều lần không?

**Đáp án dự kiến:** Không.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-1 nêu rõ tham số yêu cầu và phản hồi KHÔNG ĐƯỢC xuất hiện nhiều hơn một lần.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 7, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [10879, 11118).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
Parameters sent without a value MUST be treated as if they were
   omitted from the request.  The authorization server MUST ignore
   unrecognized request parameters.  Request and response parameters
   MUST NOT be included more than once.
```

**Hạng 2:** đơn vị nguồn 17, mục 4, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [28197, 28521).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
more than once.  If an authorization code is used more than
         once, the authorization server MUST deny the request and SHOULD
         revoke (when possible) all tokens previously issued based on
         that authorization code.  The authorization code is bound to
         the client identifier and redirection URI.
```

**Hạng 3:** đơn vị nguồn 13, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [21296, 21615).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
If the client omits the scope parameter when requesting
   authorization, the authorization server MUST either process the
   request using a pre-defined default value or fail the request
   indicating an invalid scope.  The authorization server SHOULD
   document its scope requirements and default value (if defined).
```

### A / q18
**Câu hỏi:** Theo mục 6, refresh token thay thế có được có scope khác token đã gửi lên không?

**Đáp án dự kiến:** Không. Scope phải giống nhau.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 chứa điều kiện cấp refresh token thay thế và yêu cầu scope giống nhau. Ở A, đầu đoạn bị cắt nhưng điều kiện và quy định cần để trả lời vẫn còn.
**Filter từ câu hỏi:** {"top_level_section": "6"}

**Hạng 1:** đơn vị nguồn 38, mục 6, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [63948, 64443).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The refresh token issued to the client.

   scope
         OPTIONAL.  The scope of the access request as described by
         Section 3.3.  The requested scope MUST NOT include any scope
         not originally granted by the resource owner, and if omitted is
         treated as equal to the scope originally granted by the
         resource owner.

   Because refresh tokens are typically long-lasting credentials used to
   request additional access tokens, the refresh token is bound to the
```

**Hạng 2:** đơn vị nguồn 39, mục 6, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [65757, 66168).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
server MAY issue a new refresh token, in which case
   the client MUST discard the old refresh token and replace it with the
   new refresh token.  The authorization server MAY revoke the old
   refresh token after issuing a new refresh token to the client.  If a
   new refresh token is issued, the refresh token scope MUST be
   identical to that of the refresh token included by the client in the
   request.
```

**Hạng 3:** đơn vị nguồn 35, mục 5, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [58075, 58572).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
refresh_token
         OPTIONAL.  The refresh token, which can be used to obtain new
         access tokens using the same authorization grant as described
         in Section 6.

   scope
         OPTIONAL, if identical to the scope requested by the client;
         otherwise, REQUIRED.  The scope of the access token as
         described by Section 3.3.

   The parameters are included in the entity-body of the HTTP response
   using the "application/json" media type as defined by [RFC4627].
```

### B / q18
**Câu hỏi:** Theo mục 6, refresh token thay thế có được có scope khác token đã gửi lên không?

**Đáp án dự kiến:** Không. Scope phải giống nhau.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 chứa điều kiện cấp refresh token thay thế và yêu cầu scope giống nhau. Ở A, đầu đoạn bị cắt nhưng điều kiện và quy định cần để trả lời vẫn còn.
**Filter từ câu hỏi:** {"top_level_section": "6"}

**Hạng 1:** đơn vị nguồn 39, mục 6, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [65739, 66168).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The authorization server MAY issue a new refresh token, in which case
   the client MUST discard the old refresh token and replace it with the
   new refresh token.  The authorization server MAY revoke the old
   refresh token after issuing a new refresh token to the client.  If a
   new refresh token is issued, the refresh token scope MUST be
   identical to that of the refresh token included by the client in the
   request.
```

**Hạng 2:** đơn vị nguồn 35, mục 5, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [58075, 58892).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
refresh_token
         OPTIONAL.  The refresh token, which can be used to obtain new
         access tokens using the same authorization grant as described
         in Section 6.

   scope
         OPTIONAL, if identical to the scope requested by the client;
         otherwise, REQUIRED.  The scope of the access token as
         described by Section 3.3.

   The parameters are included in the entity-body of the HTTP response
   using the "application/json" media type as defined by [RFC4627].  The
   parameters are serialized into a JavaScript Object Notation (JSON)
   structure by adding each parameter at the highest structure level.
   Parameter names and string values are included as JSON strings.
   Numerical values are included as JSON numbers.  The order of
   parameters does not matter and can vary.
```

**Hạng 3:** đơn vị nguồn 38, mục 6, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [63496, 64298).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
6.  Refreshing an Access Token

   If the authorization server issued a refresh token to the client, the
   client makes a refresh request to the token endpoint by adding the
   following parameters using the "application/x-www-form-urlencoded"
   format per Appendix B with a character encoding of UTF-8 in the HTTP
   request entity-body:

   grant_type
         REQUIRED.  Value MUST be set to "refresh_token".

   refresh_token
         REQUIRED.  The refresh token issued to the client.

   scope
         OPTIONAL.  The scope of the access request as described by
         Section 3.3.  The requested scope MUST NOT include any scope
         not originally granted by the resource owner, and if omitted is
         treated as equal to the scope originally granted by the
         resource owner.
```

### C / q18
**Câu hỏi:** Theo mục 6, refresh token thay thế có được có scope khác token đã gửi lên không?

**Đáp án dự kiến:** Không. Scope phải giống nhau.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 chứa điều kiện cấp refresh token thay thế và yêu cầu scope giống nhau. Ở A, đầu đoạn bị cắt nhưng điều kiện và quy định cần để trả lời vẫn còn.
**Filter từ câu hỏi:** {"top_level_section": "6"}

**Hạng 1:** đơn vị nguồn 39, mục 6, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [65739, 66168).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The authorization server MAY issue a new refresh token, in which case
   the client MUST discard the old refresh token and replace it with the
   new refresh token.  The authorization server MAY revoke the old
   refresh token after issuing a new refresh token to the client.  If a
   new refresh token is issued, the refresh token scope MUST be
   identical to that of the refresh token included by the client in the
   request.
```

**Hạng 2:** đơn vị nguồn 38, mục 6, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [63496, 64298).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
6.  Refreshing an Access Token

   If the authorization server issued a refresh token to the client, the
   client makes a refresh request to the token endpoint by adding the
   following parameters using the "application/x-www-form-urlencoded"
   format per Appendix B with a character encoding of UTF-8 in the HTTP
   request entity-body:

   grant_type
         REQUIRED.  Value MUST be set to "refresh_token".

   refresh_token
         REQUIRED.  The refresh token issued to the client.

   scope
         OPTIONAL.  The scope of the access request as described by
         Section 3.3.  The requested scope MUST NOT include any scope
         not originally granted by the resource owner, and if omitted is
         treated as equal to the scope originally granted by the
         resource owner.
```

**Hạng 3:** đơn vị nguồn 38, mục 6, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [64303, 64855).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
Because refresh tokens are typically long-lasting credentials used to
   request additional access tokens, the refresh token is bound to the
   client to which it was issued.  If the client type is confidential or
   the client was issued client credentials (or assigned other
   authentication requirements), the client MUST authenticate with the
   authorization server as described in Section 3.2.1.

   For example, the client makes the following HTTP request using
   transport-layer security (with extra line breaks for display purposes
   only):
```

### A / q19
**Câu hỏi:** Resource server phải kiểm tra gì khi client đưa ra access token?

**Đáp án dự kiến:** Xác minh token hợp lệ, chưa hết hạn và scope bao phủ tài nguyên được yêu cầu.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 nêu đủ yêu cầu xác minh token, kiểm tra hết hạn và phạm vi scope. A cắt phần cuối câu giải thích thêm, nhưng các câu chứa đáp án vẫn đầy đủ.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 30, mục 4, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [49708, 49862).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
(C)  The authorization server authenticates the client and validates
        the resource owner credentials, and if valid, issues an access
        token.
```

**Hạng 2:** đơn vị nguồn 40, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [66722, 67101).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The method in which the client utilizes the access token to
   authenticate with the resource server depends on the type of access
   token issued by the authorization server.  Typically, it involves
   using the HTTP "Authorization" request header field [RFC2617] with an
   authentication scheme defined by the specification of the access
   token type used, such as [RFC6750].
```

**Hạng 3:** đơn vị nguồn 39, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [66170, 66670).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
7.  Accessing Protected Resources

   The client accesses protected resources by presenting the access
   token to the resource server.  The resource server MUST validate the
   access token and ensure that it has not expired and that its scope
   covers the requested resource.  The methods used by the resource
   server to validate the access token (as well as any error responses)
   are beyond the scope of this specification but generally involve an
   interaction or coordination between the r
```

### B / q19
**Câu hỏi:** Resource server phải kiểm tra gì khi client đưa ra access token?

**Đáp án dự kiến:** Xác minh token hợp lệ, chưa hết hạn và scope bao phủ tài nguyên được yêu cầu.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 nêu đủ yêu cầu xác minh token, kiểm tra hết hạn và phạm vi scope. A cắt phần cuối câu giải thích thêm, nhưng các câu chứa đáp án vẫn đầy đủ.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 30, mục 4, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [49708, 49862).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
(C)  The authorization server authenticates the client and validates
        the resource owner credentials, and if valid, issues an access
        token.
```

**Hạng 2:** đơn vị nguồn 39, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [66170, 66717).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
7.  Accessing Protected Resources

   The client accesses protected resources by presenting the access
   token to the resource server.  The resource server MUST validate the
   access token and ensure that it has not expired and that its scope
   covers the requested resource.  The methods used by the resource
   server to validate the access token (as well as any error responses)
   are beyond the scope of this specification but generally involve an
   interaction or coordination between the resource server and the
   authorization server.
```

**Hạng 3:** đơn vị nguồn 40, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [66722, 67101).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The method in which the client utilizes the access token to
   authenticate with the resource server depends on the type of access
   token issued by the authorization server.  Typically, it involves
   using the HTTP "Authorization" request header field [RFC2617] with an
   authentication scheme defined by the specification of the access
   token type used, such as [RFC6750].
```

### C / q19
**Câu hỏi:** Resource server phải kiểm tra gì khi client đưa ra access token?

**Đáp án dự kiến:** Xác minh token hợp lệ, chưa hết hạn và scope bao phủ tài nguyên được yêu cầu.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 nêu đủ yêu cầu xác minh token, kiểm tra hết hạn và phạm vi scope. A cắt phần cuối câu giải thích thêm, nhưng các câu chứa đáp án vẫn đầy đủ.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 30, mục 4, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [49708, 49862).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
(C)  The authorization server authenticates the client and validates
        the resource owner credentials, and if valid, issues an access
        token.
```

**Hạng 2:** đơn vị nguồn 39, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [66170, 66717).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
7.  Accessing Protected Resources

   The client accesses protected resources by presenting the access
   token to the resource server.  The resource server MUST validate the
   access token and ensure that it has not expired and that its scope
   covers the requested resource.  The methods used by the resource
   server to validate the access token (as well as any error responses)
   are beyond the scope of this specification but generally involve an
   interaction or coordination between the resource server and the
   authorization server.
```

**Hạng 3:** đơn vị nguồn 40, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [66722, 67101).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The method in which the client utilizes the access token to
   authenticate with the resource server depends on the type of access
   token issued by the authorization server.  Typically, it involves
   using the HTTP "Authorization" request header field [RFC2617] with an
   authentication scheme defined by the specification of the access
   token type used, such as [RFC6750].
```

### A / q20
**Câu hỏi:** Client phải xử lý tên giá trị không nhận biết trong phản hồi token như thế nào?

**Đáp án dự kiến:** Bỏ qua các tên giá trị đó.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 nêu rõ client PHẢI bỏ qua tên giá trị không nhận biết trong phản hồi.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 35, mục 5, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [58972, 59472).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
header field [RFC2616] with a value of "no-store" in any
   response containing tokens, credentials, or other sensitive
   information, as well as the "Pragma" response header field [RFC2616]
   with a value of "no-cache".

   For example:

     HTTP/1.1 200 OK
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "access_token":"2YotnFZFEjr1zCsicMWpAA",
       "token_type":"example",
       "expires_in":3600,
       "refresh_token":"
```

**Hạng 2:** đơn vị nguồn 12, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [19666, 20161).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
MAY use the "client_id" request parameter to identify itself
   when sending requests to the token endpoint.  In the
   "authorization_code" "grant_type" request to the token endpoint, an
   unauthenticated client MUST send its "client_id" to prevent itself
   from inadvertently accepting a code intended for a client with a
   different "client_id".  This protects the client from substitution of
   the authentication code.  (It provides no additional security for the
   protected resource.)
```

**Hạng 3:** đơn vị nguồn 35, mục 5, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [59429, 59862).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
"expires_in":3600,
       "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
       "example_parameter":"example_value"
     }

   The client MUST ignore unrecognized value names in the response.  The
   sizes of tokens and other values received from the authorization
   server are left undefined.  The client should avoid making
   assumptions about value sizes.  The authorization server SHOULD
   document the size of any value it issues.
```

### B / q20
**Câu hỏi:** Client phải xử lý tên giá trị không nhận biết trong phản hồi token như thế nào?

**Đáp án dự kiến:** Bỏ qua các tên giá trị đó.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 nêu rõ client PHẢI bỏ qua tên giá trị không nhận biết trong phản hồi.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 35, mục 5, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [58897, 59862).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The authorization server MUST include the HTTP "Cache-Control"
   response header field [RFC2616] with a value of "no-store" in any
   response containing tokens, credentials, or other sensitive
   information, as well as the "Pragma" response header field [RFC2616]
   with a value of "no-cache".

   For example:

     HTTP/1.1 200 OK
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "access_token":"2YotnFZFEjr1zCsicMWpAA",
       "token_type":"example",
       "expires_in":3600,
       "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
       "example_parameter":"example_value"
     }

   The client MUST ignore unrecognized value names in the response.  The
   sizes of tokens and other values received from the authorization
   server are left undefined.  The client should avoid making
   assumptions about value sizes.  The authorization server SHOULD
   document the size of any value it issues.
```

**Hạng 2:** đơn vị nguồn 41, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [68537, 69355).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
7.2.  Error Response

   If a resource access request fails, the resource server SHOULD inform
   the client of the error.  While the specifics of such error responses
   are beyond the scope of this specification, this document establishes
   a common registry in Section 11.4 for error values to be shared among
   OAuth token authentication schemes.

   New authentication schemes designed primarily for OAuth token
   authentication SHOULD define a mechanism for providing an error
   status code to the client, in which the error values allowed are
   registered in the error registry established by this specification.

   Such schemes MAY limit the set of valid error codes to a subset of
   the registered values.  If the error code is returned using a named
   parameter, the parameter name SHOULD be "error".
```

**Hạng 3:** đơn vị nguồn 11, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [17910, 18499).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
Since requests to the token endpoint result in the transmission of
   clear-text credentials (in the HTTP request and response), the
   authorization server MUST require the use of TLS as described in
   Section 1.6 when sending requests to the token endpoint.

   The client MUST use the HTTP "POST" method when making access token
   requests.

   Parameters sent without a value MUST be treated as if they were
   omitted from the request.  The authorization server MUST ignore
   unrecognized request parameters.  Request and response parameters
   MUST NOT be included more than once.
```

### C / q20
**Câu hỏi:** Client phải xử lý tên giá trị không nhận biết trong phản hồi token như thế nào?

**Đáp án dự kiến:** Bỏ qua các tên giá trị đó.
**Điểm grounding có AI hỗ trợ: 2/2.** Lý do: Top-3 nêu rõ client PHẢI bỏ qua tên giá trị không nhận biết trong phản hồi.
**Filter từ câu hỏi:** Không có.

**Hạng 1:** đơn vị nguồn 35, mục 5, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [58897, 59862).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
The authorization server MUST include the HTTP "Cache-Control"
   response header field [RFC2616] with a value of "no-store" in any
   response containing tokens, credentials, or other sensitive
   information, as well as the "Pragma" response header field [RFC2616]
   with a value of "no-cache".

   For example:

     HTTP/1.1 200 OK
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "access_token":"2YotnFZFEjr1zCsicMWpAA",
       "token_type":"example",
       "expires_in":3600,
       "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
       "example_parameter":"example_value"
     }

   The client MUST ignore unrecognized value names in the response.  The
   sizes of tokens and other values received from the authorization
   server are left undefined.  The client should avoid making
   assumptions about value sizes.  The authorization server SHOULD
   document the size of any value it issues.
```

**Hạng 2:** đơn vị nguồn 41, mục 7, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [68537, 69355).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
7.2.  Error Response

   If a resource access request fails, the resource server SHOULD inform
   the client of the error.  While the specifics of such error responses
   are beyond the scope of this specification, this document establishes
   a common registry in Section 11.4 for error values to be shared among
   OAuth token authentication schemes.

   New authentication schemes designed primarily for OAuth token
   authentication SHOULD define a mechanism for providing an error
   status code to the client, in which the error values allowed are
   registered in the error registry established by this specification.

   Such schemes MAY limit the set of valid error codes to a subset of
   the registered values.  If the error code is returned using a named
   parameter, the parameter name SHOULD be "error".
```

**Hạng 3:** đơn vị nguồn 11, mục 3, nguồn `data/oauth2_sections_2_to_7.txt`, khoảng ký tự [17910, 18499).
Đối chiếu metadata: nguồn, ID tài liệu, đơn vị chứa chunk, text tại vị trí ký tự và mục của chunk đều khớp theo kiểm tra chương trình.

```text
Since requests to the token endpoint result in the transmission of
   clear-text credentials (in the HTTP request and response), the
   authorization server MUST require the use of TLS as described in
   Section 1.6 when sending requests to the token endpoint.

   The client MUST use the HTTP "POST" method when making access token
   requests.

   Parameters sent without a value MUST be treated as if they were
   omitted from the request.  The authorization server MUST ignore
   unrecognized request parameters.  Request and response parameters
   MUST NOT be included more than once.
```

## Diễn giải và phần xác nhận của học viên

Ở A, q18 và q19 có đủ các câu chứa đáp án dù không khớp trọn đoạn gold quote. Vì vậy điểm grounding là 2 trong khi metric evidence tự động có thể không hit; hồ sơ không sửa metric gốc. B/C có điểm coherence giống nhau vì dùng cùng chunk. Điểm grounding được đánh giá từ việc đọc top-3, không sao chép từ Hit@3.
